"""
 Created by Sakura.Gaara on  2020/12/1 17:58
"""
import logging
import os.path
import time

VIEW_LOG_PATH='logs'


def mkdir(dir):
    if not os.path.exists(dir) and not os.path.isdir(dir):
        os.mkdir(dir)


def nowtime():
    return time.strftime("%Y%m%d", time.localtime())


class Loger:
    def __init__(self, level=''):
        self.logger=logging.getLogger("")
        self.logger.handlers.clear()

        mkdir(VIEW_LOG_PATH)

        timestamp=nowtime()
        logfilename="%s.log" % (timestamp)
        logfilepath=os.path.join(VIEW_LOG_PATH,logfilename)
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        rotatingFileHandler=logging.FileHandler(logfilepath,mode='a')
        rotatingFileHandler.setFormatter(formatter)

        console=logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)

        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)



#
# logger=Loger()
#
# logger.info("aaa")

