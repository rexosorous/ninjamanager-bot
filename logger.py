from PyQt5 import QtCore
import os

class Logger(QtCore.QObject):
    log_signal = QtCore.pyqtSignal(str, str) # this has to be here for some reason

    def __init__(self, browser: str):
        super().__init__()
        if os.path.exists('json_txt/' + browser + '_log.txt'): # don't append to the last log
            os.remove('json_txt/' + browser + '_log.txt')

        self.browser = browser
        self.logger = open('json_txt/' + browser + '_log.txt', 'a+')

    def log(self, msg: str):
        # prints to gui log and log.txt
        self.logger.write(msg + '\n')
        self.log_signal.emit(self.browser, msg)

    def close(self):
        # gracefully closes connection
        self.logger.close()