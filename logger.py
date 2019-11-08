import os

class Logger():
    def __init__(self, browser: str, signals):
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