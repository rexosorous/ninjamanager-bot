import os
from PyQt5.QtWidgets import QTextBrowser

class Logger():
    def __init__(self, browser: str, gui_log):
        if os.path.exists('json_txt/' + browser + '_log.txt'): # don't append to the last log
            os.remove('json_txt/' + browser + '_log.txt')

        self.gui_log = gui_log
        self.logger = open('json_txt/' + browser + '_log.txt', 'a+')

    def log(self, msg: str):
        # prints to console and log.txt
        self.gui_log.append(msg)
        self.logger.write(msg + '\n')

    def close(self):
        # gracefully closes connection
        self.logger.close()