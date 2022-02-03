from asyncio.log import logger
import datetime
import traceback


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, logger) -> None:
        self.logger = logger
    
    def __call__(self, *args, **kwds):
        info = f'[{datetime.datetime.now()}] [INFO] [{traceback.extract_stack(None, 2)[0][2]}]\n'
        with open('logger.txt', 'a') as log:
            log.write(info)


log = Logger(logger=logger)