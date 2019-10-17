import os

class Logger():
    if os.path.exists('log.txt'): # don't append to the last log
        os.remove('log.txt')

    self.logger = open('log.txt', 'a+')

    def log(msg: str):
        # prints to console and log.txt
        print(msg)
        self.logger.write(msg)

    def close():
        # gracefully closes connection
        self.logger.close()