import os

class Logger():
    def __init__(self):
        if os.path.exists('log.txt'): # don't append to the last log
            os.remove('log.txt')

        self.logger = open('log.txt', 'a+')

    def log(self, msg: str):
        # prints to console and log.txt
        print(msg)
        self.logger.write(msg + '\n')

    def close(self):
        # gracefully closes connection
        self.logger.close()