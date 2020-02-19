from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from sys import exit
import traceback
import os

# my modules
import general.db_handler as db_handler
import general.signals as signals
import general.logger as logger
import options_window
import main_window


'''
TO DO
* implement multiprocessessing instead of threading
* implement logging module
* handle loss of internet somehow
* build a better system to stop the bot
* when item toggles, change sizehint and resize properly
* make tables sortable
* add chrome and firefox icons
'''


class GUI():
    def __init__(self, loggers, stats, signals, db):
        # pyqt definitions
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        self.app = QApplication([])
        self.app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

        # variables received
        self.loggers = loggers
        self.stats = stats
        self.signals = signals
        self.db = db

        # windows
        self.main = main_window.MainWindow(self.loggers, self.stats, self.signals, self.db)
        self.options = options_window.OptionsWindow(self.signals, self.db)

        # init
        self.connect_events()

        # start
        self.main.window.show()
        exit(self.app.exec_())



    def connect_events(self):
        self.main.contents.chrome_options.clicked.connect(self.show_options)
        self.main.contents.firefox_options.clicked.connect(self.show_options)



    def show_options(self):
        self.options.fill_fields()
        self.options.window.show()






if __name__ == "__main__":
    signals = signals.Signals()
    db = db_handler.DBHandler(signals)

    loggers = {
        'chrome': logger.Logger('chrome', signals),
        'firefox': logger.Logger('firefox', signals)
    }


    stats = {
        'chrome': {
            'gold': 0,
            'gold_gained': 0,
            'loop_count': 0,
            'arena_battles': 0,
            'world_successes': 0,
            'world_losses': 0,
            'items_gained': {},
            'ninjas': {}
        },
        'firefox': {
            'gold': 0,
            'gold_gained': 0,
            'loop_count': 0,
            'arena_battles': 0,
            'world_successes': 0,
            'world_losses': 0,
            'items_gained': {},
            'ninjas': {}
        }
    }


    try:
        gui = GUI(loggers, stats, signals, db)
    except Exception as e:
        error_string = '\n\n\n\n\n' + str(e) + '\n' + str(traceback.format_exc())
        with open('FATAL_ERROR.txt', 'w+') as file:
            file.write(error_string)
    finally:
        for logger in loggers:
            loggers[logger].close()