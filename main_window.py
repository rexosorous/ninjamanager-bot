from PyQt5.QtGui import QTextCursor
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import threading

# my modules
from general.exceptions import *
import general.utilities as util
import GUI.main_ui as main_ui
import nmbot



class MainWindow:
    def __init__(self, loggers, stats, signals, db):
        # pyqt definitions
        self.window = QtWidgets.QMainWindow()
        self.contents = main_ui.Ui_main_window()
        self.contents.setupUi(self.window)

        # variables received
        self.loggers = loggers
        self.stats = stats
        self.signals = signals
        self.db = db

        # variables created
        self.browsers = {}

        # init
        self.connect_events()
        self.ui_changes()
        self.init_recipe()





################## INIT ##################

    def connect_events(self):
        # chrome
        self.contents.chrome_item_toggle.clicked.connect(partial(self.toggle_item, self.contents.chrome_item_frame))
        self.contents.chrome_start.clicked.connect(partial(self.start, 'chrome'))
        self.contents.chrome_stop.clicked.connect(partial(self.stop, 'chrome'))
        self.contents.chrome_items.currentItemChanged.connect(partial(self.display_location, self.contents.chrome_locations))
        self.contents.chrome_world_shortcut.clicked.connect(partial(self.change_mission, self.contents.chrome_locations, 'chrome'))

        # firefox
        self.contents.firefox_item_toggle.clicked.connect(partial(self.toggle_item, self.contents.firefox_item_frame))
        self.contents.firefox_start.clicked.connect(partial(self.start, 'firefox'))
        self.contents.firefox_stop.clicked.connect(partial(self.stop, 'firefox'))
        self.contents.firefox_items.currentItemChanged.connect(partial(self.display_location, self.contents.firefox_locations))
        self.contents.firefox_world_shortcut.clicked.connect(partial(self.change_mission, self.contents.firefox_locations, 'firefox'))

        # signals
        self.signals.log_signal.connect(self.main_log)
        self.signals.info_signal.connect(self.update_info)
        self.signals.ninja_signal.connect(self.update_ninjas)
        self.signals.options_signal.connect(self.update_options)
        self.signals.pin_signal.connect(self.pin_recipe)
        self.signals.options_msg_signal.connect(self.log)



    def ui_changes(self):
        # additional changes to the ui
        self.contents.chrome_log.ensureCursorVisible()
        self.contents.firefox_log.ensureCursorVisible()

        self.contents.chrome_locations.hideColumn(2)
        self.contents.chrome_locations.hideColumn(3)
        self.contents.firefox_locations.hideColumn(2)
        self.contents.firefox_locations.hideColumn(3)

        # resizing
        self.contents.chrome_ninjas.setColumnWidth(0, 136)
        self.contents.firefox_ninjas.setColumnWidth(0, 136)
        self.contents.chrome_ninjas.setColumnWidth(1, 75)
        self.contents.firefox_ninjas.setColumnWidth(1, 75)
        self.contents.chrome_ninjas.setColumnWidth(2, 75)
        self.contents.firefox_ninjas.setColumnWidth(2, 75)

        self.contents.chrome_recipe.setColumnWidth(0, 190)
        self.contents.firefox_recipe.setColumnWidth(0, 190)
        self.contents.chrome_recipe.setColumnWidth(1, 75)
        self.contents.firefox_recipe.setColumnWidth(1, 75)

        self.contents.chrome_locations.setColumnWidth(0, 190)
        self.contents.firefox_locations.setColumnWidth(0, 190)
        self.contents.chrome_locations.setColumnWidth(1,70)
        self.contents.firefox_locations.setColumnWidth(1, 70)


    def init_recipe(self):
        # fills the item helper areas from data in config.json
        # get data
        data = util.get_options()

        table_picker = {
            'chrome': self.contents.chrome_items,
            'firefox': self.contents.firefox_items
        }

        tree_picker = {
            'chrome': self.contents.chrome_recipe,
            'firefox': self.contents.firefox_recipe
        }

        # we connect signal here to avoid calling update_full_recipe when user interacts with options window
        self.signals.recipe_signal.connect(self.update_full_recipe)

        # fill chrome_items table
        for browser in table_picker:
            if data[browser]['LW']:
                self.browser = browser # need this so update_full_recipe knows which to update
                tree_picker[browser].addTopLevelItem(QtWidgets.QTreeWidgetItem([data[browser]['LW'], '1']))
                total_basic_items = self.db.find_recipe(data[browser]['LW'], 1)
                for item in total_basic_items:
                    table_picker[browser].addItem(item + ': ' + str(total_basic_items[item]))
                tree_picker[browser].expandAll()
                table_picker[browser].sortItems()

        del self.browser
        self.signals.recipe_signal.disconnect(self.update_full_recipe)



    def update_full_recipe(self, parent_name, child_name, child_amount):
        # updates full recipe tree widget
        tree_picker = {
            'chrome': self.contents.chrome_recipe,
            'firefox': self.contents.firefox_recipe
        }

        parent = tree_picker[self.browser].findItems(parent_name, Qt.MatchRecursive)[0]
        parent.addChild(QtWidgets.QTreeWidgetItem([child_name, str(child_amount)]))










################## EVENTS ##################

    def start(self, browser: str):
        # makes a thread for the browser to stop main from freezing
        if browser in self.browsers.keys(): # if browser is in the dict
            if self.browsers[browser]: # if the value at browser exists
                return # don't restart the bot

        browser_thread = threading.Thread(target=self.start_browser, args=[browser])
        browser_thread.daemon = True
        browser_thread.start()




    def start_browser(self, browser: str):
        # starts selenium
        try:
            self.browsers[browser] = nmbot.NMBot(self.stats[browser], self.loggers[browser], self.signals, browser)
            self.browsers[browser].execute()
        except LoginFailure:
            self.loggers[browser].log('LOGIN FAILED\naborting ...')
            self.browsers[browser].stop()
            del self.browsers[browser]



    def stop(self, browser: str):
        if browser in self.browsers.keys():
            self.browsers[browser].stop()
            self.signals.info_signal.emit()
            del self.browsers[browser]



    def toggle_item(self, gui_object):
        # shows and hides the item helper in main window
        if gui_object.isVisible():
            gui_object.hide()
        else:
            gui_object.show()



    def main_log(self, browser: str, msg: str):
        log_picker = {'chrome': self.contents.chrome_log, 'firefox': self.contents.firefox_log}
        log_picker[browser].append(msg)
        log_picker[browser].moveCursor(QTextCursor.End)



    def update_info(self):
        # updates info in main
        self.contents.chrome_loop_count.setText(str(self.stats['chrome']['loop_count']))
        self.contents.chrome_gold_gained.setText(str(self.stats['chrome']['gold_gained']))
        self.contents.chrome_arena_battles.setText(str(self.stats['chrome']['arena_battles']))
        self.contents.chrome_world_wins.setText(str(self.stats['chrome']['world_successes']))
        self.contents.chrome_world_losses.setText(str(self.stats['chrome']['world_losses']))

        chrome_items = ''
        for item in self.stats['chrome']['items_gained']:
            chrome_items += str(item + ': ' + str(self.stats['chrome']['items_gained'][item]))
        self.contents.chrome_items_gained.setText(chrome_items)


        self.contents.firefox_loop_count.setText(str(self.stats['firefox']['loop_count']))
        self.contents.firefox_gold_gained.setText(str(self.stats['firefox']['gold_gained']))
        self.contents.firefox_arena_battles.setText(str(self.stats['firefox']['arena_battles']))
        self.contents.firefox_world_wins.setText(str(self.stats['firefox']['world_successes']))
        self.contents.firefox_world_losses.setText(str(self.stats['firefox']['world_losses']))

        firefox_items = ''
        for item in self.stats['firefox']['items_gained']:
            firefox_items += str(item + ': ' + str(self.stats['firefox']['items_gained'][item]))
        self.contents.firefox_items_gained.setText(firefox_items)



    def update_ninjas(self, ninjas: dict, browser: str):
        # updates the info on ninja exp in main
        ninja_table = {'chrome': self.contents.chrome_ninjas, 'firefox': self.contents.firefox_ninjas}

        # clear table
        for row in range(ninja_table[browser].rowCount()):
            ninja_table[browser].removeRow(0)

        row = 0
        for name, lvl in ninjas.items():
            if lvl != self.stats[browser]['ninjas'][name]:
                old = self.stats[browser]['ninjas'][name]

                old_lvl = old[:old.find('@')]
                old_exp = old[old.find('@')+1:]
                old_total = int(old_lvl + old_exp[:-1])

                new_lvl = lvl[:lvl.find('@')]
                new_exp = lvl[lvl.find('@')+1:]
                new_total = int(new_lvl + new_exp[:-1])

                ninja_table[browser].insertRow(row)
                ninja_table[browser].setItem(row, 0, QtWidgets.QTableWidgetItem(name))
                ninja_table[browser].setItem(row, 1, QtWidgets.QTableWidgetItem('lv.' + new_lvl + '@' + new_exp))
                ninja_table[browser].setItem(row, 2, QtWidgets.QTableWidgetItem(str(new_total-old_total) + '%'))

                row += 1



    def update_options(self, data: dict):
        # updates the world mission and cooldown
        for browser in self.browsers:
            self.browsers[browser].update_options(data)



    def pin_recipe(self, data: dict, browser: str):
        gui_picker = {
            'chrome': {
                'recipe': self.contents.chrome_recipe,
                'items': self.contents.chrome_items
            },
            'firefox': {
                'recipe': self.contents.firefox_recipe,
                'items': self.contents.firefox_items
            }
        }

        gui_picker[browser]['recipe'].addTopLevelItem(data['recipe'])
        gui_picker[browser]['recipe'].expandAll()

        gui_picker['chrome']['items'].addItem(data['chrome']['items'])
        gui_picker['firefox']['items'].addItem(data['firefox']['items'])



    def display_location(self, gui_object, table_item, old_item):
        # when user clicks on a basic item, display where you can get it
        # clear the table
        for row in range(gui_object.rowCount()):
            gui_object.removeRow(0)

        # get data
        item_name = table_item.text()[:table_item.text().find(':')]
        all_locations = self.db.find_locations(item_name)

        # populate table
        for row in range(len(all_locations)):
            gui_object.insertRow(row)
            gui_object.setItem(row, 0, QtWidgets.QTableWidgetItem(util.fix_location(all_locations[row])))
            gui_object.setItem(row, 1, QtWidgets.QTableWidgetItem(all_locations[row]['chance']))
            gui_object.setItem(row, 2, QtWidgets.QTableWidgetItem(all_locations[row]['location']))
            gui_object.setItem(row, 3, QtWidgets.QTableWidgetItem(all_locations[row]['mission']))



    def change_mission(self, gui_object, browser: str):
        row = gui_object.currentRow()
        url = gui_object.item(row, 2).text()
        mission = gui_object.item(row, 3).text()

        data = util.get_options()
        data[browser]['world']['area_url'] = url
        data[browser]['world']['mission_num'] = mission
        util.save_options(data)

        self.signals.options_signal.emit(data)



    def log(self, msg: str, browser: str):
        self.loggers[browser].log(msg)