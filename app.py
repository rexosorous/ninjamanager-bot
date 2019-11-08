from PyQt5.QtGui import QTextCursor
from functools import partial
from PyQt5 import QtWidgets
from sys import exit
import traceback
import threading
import json
import os

from exceptions import *
import signals
import main_ui
import logger
import nmbot

# TO DO
# implement databases
# error checking for incorrect mission data
# legendary weapon grinding



class GUI():
    def __init__(self, loggers, stats):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.gui = main_ui.Ui_main_window()
        self.gui.setupUi(self.window)

        self.signals = signals.Signals()
        self.browsers = {}
        self.accounts = self.get_accounts()
        self.cookies = self.get_cookies()
        self.stats = stats
        self.loggers = loggers
        self.loggers['chrome'] = logger.Logger('chrome', self.signals)
        self.loggers['firefox'] = logger.Logger('firefox', self.signals)
        self.log_picker = {'chrome': self.gui.chrome_log, 'firefox': self.gui.firefox_log}

        self.connect_buttons()
        self.ui_changes()
        self.window.show()

        self.signals.info_signal.emit()

        exit(self.app.exec_())



    def connect_buttons(self):
        self.gui.chrome_log_toggle.clicked.connect(partial(self.toggle_log, 'chrome'))
        self.gui.chrome_start.clicked.connect(partial(self.start, 'chrome'))
        self.gui.chrome_stop.clicked.connect(partial(self.stop, 'chrome'))
        self.gui.chrome_mission_submit.clicked.connect(partial(self.change_mission, 'chrome'))
        self.gui.chrome_cooldown_submit.clicked.connect(partial(self.change_cooldown, 'chrome'))

        self.gui.firefox_log_toggle.clicked.connect(partial(self.toggle_log, 'firefox'))
        self.gui.firefox_start.clicked.connect(partial(self.start, 'firefox'))
        self.gui.firefox_stop.clicked.connect(partial(self.stop, 'firefox'))
        self.gui.firefox_mission_submit.clicked.connect(partial(self.change_mission, 'firefox'))
        self.gui.firefox_cooldown_submit.clicked.connect(partial(self.change_cooldown, 'firefox'))

        # self.loggers['chrome'].log_signal.connect(self.gui_log)
        # self.loggers['firefox'].log_signal.connect(self.gui_log)
        self.signals.log_signal.connect(self.gui_log)
        self.signals.info_signal.connect(self.update_info)



    def ui_changes(self):
        # additional changes to the ui
        self.gui.chrome_log.ensureCursorVisible()
        self.gui.firefox_log.ensureCursorVisible()



    def start(self, browser: str):
        # makes a thread for the browser to stop gui from freezing
        if browser in self.browsers.keys(): # if browser is in the dict
            if self.browsers[browser]: # if the value at browser exists
                return # don't restart the bot

        browser_thread = threading.Thread(target=self.start_browser, args=[browser])
        browser_thread.daemon = True
        browser_thread.start()




    def start_browser(self, browser: str):
        # starts selenium
        try:
            self.browsers[browser] = nmbot.NMBot(self.accounts[browser], self.cookies[browser], self.stats[browser], self.loggers[browser], browser, self.signals)
            self.browsers[browser].execute()
        except LoginFailure:
            self.loggers[browser].log('LOGIN FAILED\naborting ...')
            self.browsers[browser].stop()
            del self.browsers[browser]



    def stop(self, browser: str):
        if browser in self.browsers.keys():
            self.browsers[browser].check_gold()
            self.browsers[browser].stop()
            self.loggers[browser].log(get_stats(self.stats, browser))
            self.signals.info_signal.emit()
            del self.browsers[browser]



    def change_mission(self, browser: str):
        mission_data = {}

        if browser == 'chrome':
            mission_data['area_url'] = self.gui.chrome_area.displayText()
            mission_data['mission_num'] = self.gui.chrome_mission_num.displayText()
        elif browser == 'firefox':
            mission_data['area_url'] = self.gui.firefox_area.displayText()
            mission_data['mission_num'] = self.gui.firefox_mission_num.displayText()

        for key in mission_data: # make sure all fields are filled
            if key == '':
                return

        # clear fields
        self.gui.chrome_area.clear()
        self.gui.chrome_mission_num.clear()
        self.gui.firefox_area.clear()
        self.gui.firefox_mission_num.clear()

        # save data
        with open('json_txt/options.json', 'r') as file:
            data = json.load(file)

        data['world'][browser] = mission_data
        with open('json_txt/options.json', 'w') as file:
            json.dump(data, file)

        if browser in self.browsers.keys(): # allow updating without program running
            self.browsers[browser].load_mission(browser)
            self.browsers[browser].logger.log('\nupdated mission data')



    def change_cooldown(self, browser: str):
        # changes the time between arena and world actions in MINUTES
        cooldown_data = {}

        try:
            if browser == 'chrome':
                cooldown_data['lower'] = float(self.gui.chrome_cooldown_lower.displayText()) * 60
                cooldown_data['upper'] = float(self.gui.chrome_cooldown_upper.displayText()) * 60
            elif browser == 'firefox':
                cooldown_data['lower'] = float(self.gui.firefox_cooldown_lower.displayText()) * 60
                cooldown_data['upper'] = float(self.gui.firefox_cooldown_upper.displayText()) * 60
        except ValueError:
            return

        for key in cooldown_data: # make sure all fields are filled
            if key == '':
                return

        # clear fields
        self.gui.chrome_cooldown_lower.clear()
        self.gui.chrome_cooldown_upper.clear()
        self.gui.firefox_cooldown_lower.clear()
        self.gui.firefox_cooldown_upper.clear()

        # save data
        with open('json_txt/options.json', 'r') as file:
            data = json.load(file)

        data['cooldown'][browser] = cooldown_data
        with open('json_txt/options.json', 'w') as file:
            json.dump(data, file)

        if browser in self.browsers.keys():
            self.browsers[browser].load_cooldown(browser)
            self.bwowsers[browser].logger.log('\nupdated cooldown')



    def get_accounts(self):
        with open('json_txt/accounts.json', 'r') as file:
            accounts = json.load(file)
        return accounts



    def get_cookies(self):
        with open('json_txt/cookies.json', 'r') as file:
            cookies = json.load(file)
        return cookies



    def toggle_log(self, browser: str):
        # shows and hides the log in gui
        if self.log_picker[browser].isVisible():
            self.log_picker[browser].hide()
        else:
            self.log_picker[browser].show()
        self.window.resize(self.window.minimumSizeHint())



    def gui_log(self, browser: str, msg: str):
        self.log_picker[browser].append(msg)
        self.log_picker[browser].moveCursor(QTextCursor.End)



    def update_info_loop(self):
        # we need to emit a signal to update info in the gui because pyqt5 doesn't play nice with threading
        while True:
            self.info_signal.info_signal.emit()
            sleep(15)



    def update_info(self):
        # updates info in gui
        self.gui.chrome_loop_count.setText(str(stats['chrome']['loop_count']))
        self.gui.chrome_gold_gained.setText(str(stats['chrome']['gold_gained']))
        self.gui.chrome_arena_battles.setText(str(stats['chrome']['arena_battles']))
        self.gui.chrome_world_wins.setText(str(stats['chrome']['world_successes']))
        self.gui.chrome_world_losses.setText(str(stats['chrome']['world_losses']))

        chrome_items = ''
        for item in stats['chrome']['items_gained']:
            chrome_items += str(item + ': ' + stats['chrome']['items_gained'][item])
        self.gui.chrome_items_gained.setText(chrome_items)


        self.gui.firefox_loop_count.setText(str(stats['firefox']['loop_count']))
        self.gui.firefox_gold_gained.setText(str(stats['firefox']['gold_gained']))
        self.gui.firefox_arena_battles.setText(str(stats['firefox']['arena_battles']))
        self.gui.firefox_world_wins.setText(str(stats['firefox']['world_successes']))
        self.gui.firefox_world_losses.setText(str(stats['firefox']['world_losses']))

        firefox_items = ''
        for item in stats['firefox']['items_gained']:
            firefox_items += str(item + ': ' + str(stats['firefox']['items_gained'][item]))
        self.gui.firefox_items_gained.setText(firefox_items)





def get_stats(stats, browser: str):
    # returns a formatted string of stats
    basic = str(browser + ' STATS' +
                          '\nTotal Loops:   ' + str(stats[browser]['loop_count']) +
                          '\nGold Gained:   ' + str(stats[browser]['gold_gained']) +
                          '\nArena Battles: ' + str(stats[browser]['arena_battles']) +
                          '\nWorld Wins:    ' + str(stats[browser]['world_successes']) +
                          '\nWorld Losses:  ' + str(stats[browser]['world_losses']) + '\n')
    items = 'Items Gained:\n'
    for item in stats[browser]['items_gained']:
        items += str('                ' + item + ': ' + str(stats[browser]['items_gained'][item]) + '\n')
    rstring = basic + items + '\n\n'
    return rstring






if __name__ == "__main__":
    loggers = {
        'chrome': None,
        'firefox': None
    }


    stats = {
        'chrome': {
            'gold': 0,
            'gold_gained': 0,
            'loop_count': 0,
            'arena_battles': 0,
            'world_successes': 0,
            'world_losses': 0,
            'items_gained': {}
        },
        'firefox': {
            'gold': 0,
            'gold_gained': 0,
            'loop_count': 0,
            'arena_battles': 0,
            'world_successes': 0,
            'world_losses': 0,
            'items_gained': {}
        }
    }


    try:
        gui = GUI(loggers, stats)
    except Exception as e:
        error_string = '\n\n\n\n\n' + str(e) + '\n' + traceback.format_exc()
        print(error_string)
        with open('FATAL_ERROR.txt', 'w+') as file:
            file.write(error_string)
    finally:
        for logger in loggers:
            loggers[logger].close()

        if os.path.exists('json_txt/summary.txt'):
            os.remove('json_txt/summary.txt')
        with open('json_txt/summary.txt', 'a+') as file:
            for browser in stats:
                file.write(get_stats(stats, browser))