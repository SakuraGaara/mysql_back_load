"""
 Created by Sakura.Gaara on  2020/12/1 17:58
"""
import logging
import os.path
import time
import coloredlogs
from logging.handlers import TimedRotatingFileHandler

VIEW_LOG_PATH = 'logs'

coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'hostname': {'color': 'magenta'},
                                    'levelname': {'color': 'green', 'bold': True}, 'request_id': {'color': 'yellow'},
                                    'name': {'color': 'blue'}, 'programname': {'color': 'cyan'},
                                    'threadName': {'color': 'yellow'}}


def mkdir(dir):
    if not os.path.exists(dir) and not os.path.isdir(dir):
        os.mkdir(dir)


def get_logfile(dir):
    logfilename = 'app.log'
    logfile = os.path.join(dir, logfilename)
    return logfile


class Log:
    __instances = {}

    def __init__(self):
        mkdir(VIEW_LOG_PATH)

    @classmethod
    def getLogger(cls, name='sys'):
        logfile = get_logfile(VIEW_LOG_PATH)
        if name not in cls.__instances:
            logger = logging.getLogger(name=name)

            # fmt='[%(asctime)s] [%(levelname)s] [%(name)s] %(filename)s[line:%(lineno)d] [%(threadName)s]: %(message)s'
            fmt = '[%(asctime)s] [%(hostname)s] [%(name)s] [%(process)d] %(levelname)s: %(message)s'
            formatter = logging.Formatter(fmt)

            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            console.setFormatter(formatter)
            logger.addHandler(console)

            coloredlogs.install(fmt=fmt, level=logging.INFO, logger=logger)

            fileHandler = TimedRotatingFileHandler(logfile, when='D', interval=60 * 60 * 24,
                                                   backupCount=7, encoding='utf-8')
            fileHandler.setFormatter(formatter)
            fileHandler.setLevel(logging.NOTSET)
            logger.addHandler(fileHandler)

            cls.__instances[name] = logger

        return cls.__instances[name]
