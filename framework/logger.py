import datetime
import sys

from pattern import MetaSingleton


class Logger(metaclass=MetaSingleton):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def write_log(name, message):
        with open(f'logs/{name}.log', 'a') as file:
            file.write(f'{message}\n')

    def debug(self, message):
        msg = f'[{datetime.datetime.now()}] - DEBUG - [logger name >> {self.name}] - [{message}]'
        self.write_log(self.name, msg)

    def info(self, message):
        msg = f'[{datetime.datetime.now()}] - INFO - [logger name >> {self.name}] - [{message}]'
        self.write_log(self.name, msg)

    def warning(self, message):
        msg = f'[{datetime.datetime.now()}] - WARNING - [logger name >> {self.name}] - [{message}]'
        self.write_log(self.name, msg)

    def error(self, message):
        msg = f'[{datetime.datetime.now()}] - ERROR - [logger name >> {self.name}] - [{message}]'
        self.write_log(self.name, msg)

    def critical(self, message):
        msg = f'[{datetime.datetime.now()}] - CRITICAL - [logger name >> {self.name}] - [{message}]'
        self.write_log(self.name, msg)
        sys.exit([0])


