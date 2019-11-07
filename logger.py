# from PyQt5 import QtCore
import os

class Logger():
    # log_signal = QtCore.pyqtSignal(str, str) # this has to be here for some reason

    def __init__(self, browser: str, signals):
        # super().__init__()
        self.signals = signals
        if os.path.exists('json_txt/' + browser + '_log.txt'): # don't append to the last log
            os.remove('json_txt/' + browser + '_log.txt')

        self.browser = browser
        self.logger_file = open('json_txt/' + browser + '_log.txt', 'a+')

    def log(self, msg: str):
        # prints to gui log and log.txt
        self.logger_file.write(msg + '\n')
        self.signals.log_signal.emit(self.browser, msg)

    def close(self):
        # gracefully closes connection
        self.logger_file.close()