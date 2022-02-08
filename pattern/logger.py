import logging
import datetime
import traceback


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger():
    def __init__(self, name) -> None:
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        logger_handler = logging.FileHandler(f'{self.name}.log')

        logger_handler.setLevel(logging.DEBUG)

        strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s'

        datefmt = '%Y-%m-%d %H:%M:%S'

        formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
        logger_handler.setFormatter(formatter)
        self.logger.addHandler(logger_handler)

    def __call__(self, *args, **kwargs):
        self.logger.debug(args)
