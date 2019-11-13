from PyQt5.QtCore import Qt
from functools import partial
from PyQt5 import QtWidgets
import json

import options_ui


class OptionsWindow:
    def __init__(self, signals, db):
        # pyqt definitions
        self.window = QtWidgets.QMainWindow()
        self.contents = options_ui.Ui_options_window()
        self.contents.setupUi(self.window)

        # variables received
        self.signals = signals
        self.db = db

        # variables created
        self.options = self.get_options_data()

        # init
        self.connect_events()
        self.ui_changes()
        self.fill_fields()
        self.populate_tables()



    def get_options_data(self) -> dict:
        with open('json_txt/options.json', 'r') as file:
            data = json.load(file)

        return data



    def connect_events(self):
        # chrome
        self.contents.chrome_mission_submit.clicked.connect(partial(self.change_mission, 'chrome'))
        self.contents.chrome_cooldown_submit.clicked.connect(partial(self.change_cooldown, 'chrome'))

        # firefox
        self.contents.firefox_mission_submit.clicked.connect(partial(self.change_mission, 'firefox'))
        self.contents.firefox_cooldown_submit.clicked.connect(partial(self.change_cooldown, 'firefox'))

        # general
        self.contents.chrome_dropped_lw.clicked.connect(partial(self.change_mission_lw, 'chrome'))
        self.contents.firefox_dropped_lw.clicked.connect(partial(self.change_mission_lw, 'firefox'))
        self.contents.crafted_lw.itemDoubleClicked.connect(self.display_recipe)
        self.contents.crafted_bl.itemDoubleClicked.connect(self.display_recipe)
        self.contents.chrome_pin.clicked.connect(partial(self.pin_recipe, 'chrome'))
        self.contents.firefox_pin.clicked.connect(partial(self.pin_recipe, 'firefox'))

        #signals
        self.signals.recipe_signal.connect(self.update_expanded_recipe)
        self.signals.area_signal.connect(self.update_area)
        self.signals.options_signal.connect(self.update_options)



    def ui_changes(self):
        # additional changes to the ui
        # resizing
        self.contents.dropped_lw.setColumnWidth(0, 127)
        self.contents.dropped_lw.setColumnWidth(1, 127)
        self.contents.dropped_lw.setColumnWidth(2, 75)

        self.contents.recipe.setColumnWidth(0, 190)
        self.contents.recipe.setColumnWidth(1, 75)



    def fill_fields(self):
        # fills the world mission and cooldown fields
        self.contents.chrome_area_label.setText(self.options['chrome']['world']['area_url'])
        self.contents.chrome_mission_label.setText(self.options['chrome']['world']['mission_num'])
        self.contents.chrome_cooldown_label.setText(str(self.options['chrome']['cooldown']['lower']/60) + ' - ' + str(self.options['chrome']['cooldown']['upper']/60) + ' minutes')

        self.contents.firefox_area_label.setText(self.options['firefox']['world']['area_url'])
        self.contents.firefox_mission_label.setText(self.options['firefox']['world']['mission_num'])
        self.contents.firefox_cooldown_label.setText(str(self.options['firefox']['cooldown']['lower']/60) + ' - ' + str(self.options['firefox']['cooldown']['upper']/60) + ' minutes')



    def populate_tables(self):
        # dropped lw table
        row = 0
        dropped_lws = self.db.get_dropped_lws()
        for lw in dropped_lws:
            self.contents.dropped_lw.insertRow(row)
            self.contents.dropped_lw.setItem(row, 0, QtWidgets.QTableWidgetItem(lw))
            self.contents.dropped_lw.setItem(row, 1, QtWidgets.QTableWidgetItem(self.fix_location(dropped_lws[lw])))
            self.contents.dropped_lw.setItem(row, 2, QtWidgets.QTableWidgetItem(dropped_lws[lw]['chance']))
        self.contents.dropped_lw.sortItems(0)

        # crafted lw list
        for lw in self.db.get_crafted_lws():
            self.contents.crafted_lw.addItem(lw)
        self.contents.crafted_lw.sortItems()

        # crafted bl list
        for bl in self.db.get_bls():
            self.contents.crafted_bl.addItem(bl)
        self.contents.crafted_bl.sortItems()





    def change_mission(self, browser: str):
        # changes which world mission the bot executes
        gui_picker = {
            'chrome': {
                'area': self.contents.chrome_area,
                'mission': self.contents.chrome_mission_num,
            },
            'firefox': {
                'area': self.contents.firefox_area,
                'mission': self.contents.firefox_mission_num
            }
        }

        area = gui_picker[browser]['area'].displayText()
        mission = gui_picker[browser]['mission'].displayText()

        if area and mission: # make sure the fields at least have text in them
            # save to file
            with open('json_txt/options.json', 'r') as file:
                data = json.load(file)
            data[browser]['world']['area_url'] = area
            data[browser]['world']['mission_num'] = mission
            with open('json_txt/options.json', 'w') as file:
                json.dump(data, file)

            # update data
            self.signals.options_signal.emit(data)

            # clear fields
            gui_picker[browser]['area'].clear()
            gui_picker[browser]['mission'].clear()



    def change_cooldown(self, browser: str):
        # changes the time between arena and world actions in MINUTES
        gui_picker = {
            'chrome': {
                'lower': self.contents.chrome_cooldown_lower,
                'upper': self.contents.chrome_cooldown_upper,
            },
            'firefox': {
                'lower': self.contents.firefox_cooldown_lower,
                'upper': self.contents.firefox_cooldown_upper
            }
        }

        try:
            lower = float(gui_picker[browser]['lower'].displayText()) * 60
            upper = float(gui_picker[browser]['upper'].displayText()) * 60
        except ValueError:
            return

        if lower and upper: # make sure the fields at least have text in them
            # save to file
            with open('json_txt/options.json', 'r') as file:
                data = json.load(file)
            data[browser]['cooldown']['lower'] = lower
            data[browser]['cooldown']['upper'] = upper
            with open('json_txt/options.json', 'w') as file:
                json.dump(data, file)

            # update data
            self.signals.options_signal.emit(data)

            # clear fields
            gui_picker[browser]['lower'].clear()
            gui_picker[browser]['upper'].clear()



    def change_mission_lw(self, browser):
        # sets the world mission to the highlighted item in dropped lw list
        selected_row = self.contents.dropped_lw.selectedItems() # maybe currentItem() or currentRow()?

        with open('json_txt/options.json', 'r') as file:
            data = json.load(file)
        fix_me = selected_row[1].text()
        fixed_area = fix_me[:fix_me.find('#')-1].replace(' ', '-')
        fixed_mission = fix_me[fix_me.find('#')+1:]
        data[browser]['world']['area_url'] = 'https://www.ninjamanager.com/world/area/' + fixed_area
        data[browser]['world']['mission_num'] = fixed_mission
        with open('json_txt/options.json', 'w') as file:
            json.dump(data, file)

        self.signals.options_signal.emit(data)



    def display_recipe(self, list_item):
        # when a user double clicks a legendary item or bloodline, display the recipe to craft it
        # clear areas
        self.contents.recipe.clear()
        self.contents.basic_items.clear()
        self.contents.areas.clear()

        self.contents.recipe.addTopLevelItem(QtWidgets.QTreeWidgetItem([list_item.text(), '1']))
        total_basic_items = self.db.find_recipe(list_item.text(), 1)
        for item in total_basic_items:
            self.contents.basic_items.addItem(item + ': ' + str(total_basic_items[item]))
        self.contents.recipe.expandAll()
        self.contents.basic_items.sortItems()
        self.contents.areas.sortItems()



    def update_expanded_recipe(self, parent_name, child_name, child_amount):
        # updates expanded area
        parent = self.contents.recipe.findItems(parent_name, Qt.MatchRecursive)[0]
        parent.addChild(QtWidgets.QTreeWidgetItem([child_name, str(child_amount)]))



    def update_area(self, data: dict):
        # updates required area access
        area = self.fix_location(data)
        if not self.contents.areas.findItems(area, Qt.MatchExactly):
            self.contents.areas.addItem(area)



    def update_options(self, data: dict):
        self.options = data
        self.fill_fields()



    def pin_recipe(self, browser):
        # copies contents of recipe and basic items to main window
        transfer = {}

        # recipe
        transfer['recipe'] = self.contents.recipe.takeTopLevelItem(0)

        # basic items
        transfer['items'] = []
        for row in range(len(self.contents.basic_items)):
            transfer['items'].append(self.contents.basic_items.takeItem(0))

        # clear areas
        self.contents.areas.clear()

        # output
        self.signals.pin_signal.emit(transfer, browser)

        # save so we don't have to keep selecting the LW every time we open the program
        with open('json_txt/options.json', 'r') as file:
            data = json.load(file)
        data[browser]['LW'] = transfer['recipe'].text(0)
        with open('json_txt/options.json', 'w') as file:
            json.dump(data, file)

        self.options = data



    def fix_location(self, item_data: dict) -> str:
        # makes the locations easier to read
        location = item_data['location']
        if 'Shop' in location:
            return location
        location = location[location.find('area')+5:].replace('-', ' ')
        return location + ' #' + item_data['mission']