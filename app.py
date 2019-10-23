from functools import partial
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtWidgets
from sys import exit
import traceback
import threading
import json
import os

from exceptions import *
import main_ui
import logger
import nmbot


# TO DO
# implement databases
# error checking for incorrect mission data
# gold gain from world grinding
# legendary weapon grinding



class GUI():
    def __init__(self, loggers, stats):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.gui = main_ui.Ui_main_window()
        self.gui.setupUi(self.window)

        self.browsers = {}
        self.accounts = self.get_accounts()
        self.cookies = self.get_cookies()
        self.stats = stats
        self.loggers = loggers
        self.loggers['chrome'] = logger.Logger('chrome')
        self.loggers['firefox'] = logger.Logger('firefox')

        self.connect_buttons()
        self.ui_changes()
        self.window.show()
        exit(self.app.exec_())



    def connect_buttons(self):
        self.gui.chrome_start.clicked.connect(partial(self.start, 'chrome'))
        self.gui.chrome_stop.clicked.connect(partial(self.stop, 'chrome'))
        self.gui.chrome_mission_submit.clicked.connect(partial(self.change_mission, 'chrome'))

        self.gui.firefox_start.clicked.connect(partial(self.start, 'firefox'))
        self.gui.firefox_stop.clicked.connect(partial(self.stop, 'firefox'))
        self.gui.firefox_mission_submit.clicked.connect(partial(self.change_mission, 'firefox'))

        self.loggers['chrome'].log_signal.connect(self.gui_log)
        self.loggers['firefox'].log_signal.connect(self.gui_log)



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
            self.browsers[browser] = nmbot.NMBot(self.accounts[browser], self.cookies[browser], self.stats[browser], self.loggers[browser], browser)
            self.browsers[browser].execute()
        except LoginFailure:
            self.loggers[browser].log('LOGIN FAILED\naborting ...')
            self.browsers[browser].stop()
            del self.browsers[browser]



    def stop(self, browser: str):
        if browser in self.browsers.keys():
            self.browsers[browser].stop()
            self.loggers[browser].log(get_stats(self.stats, browser))
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

        with open('json_txt/world.json', 'r') as file:
            data = json.load(file)

        data[browser] = mission_data
        with open('json_txt/world.json', 'w') as file:
            json.dump(data, file)

        if browser in self.browsers.keys(): # allow updating without program running
            self.browsers[browser].load_mission(browser)
            self.browsers[browser].logger.log('updated mission data')



    def get_accounts(self):
        with open('json_txt/accounts.json', 'r') as file:
            accounts = json.load(file)
        return accounts



    def get_cookies(self):
        with open('json_txt/cookies.json', 'r') as file:
            cookies = json.load(file)
        return cookies



    def gui_log(self, browser: str, msg: str):
        log_picker = {'chrome': self.gui.chrome_log, 'firefox': self.gui.firefox_log}
        log_picker[browser].append(msg)
        log_picker[browser].moveCursor(QTextCursor.End)





def get_stats(stats, browser: str):
    # returns a formatted string of stats
    return(str(browser + ' STATS' +
                         '\nTotal Loops:   ' + str(stats[browser]['loop_count']) +
                         '\nArena Battles: ' + str(stats[browser]['arena_battles']) +
                         '\nWorld Wins:    ' + str(stats[browser]['world_successes']) +
                         '\nWorld Losses:  ' + str(stats[browser]['world_losses']) +
                         '\nItems Gained:  ' + str(stats[browser]['item_successes']) + '\n\n'))






if __name__ == "__main__":
    loggers = {
        'chrome': None,
        'firefox': None
    }


    stats = {
        'chrome': {
            'loop_count': 0,
            'arena_battles': 0,
            'world_successes': 0,
            'world_losses': 0,
            'item_successes': 0
        },
        'firefox': {
            'loop_count': 0,
            'arena_battles': 0,
            'world_successes': 0,
            'world_losses': 0,
            'item_successes': 0
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