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
        self.make_logger_message('debug', self.name, message)

    def info(self, message):
        self.make_logger_message('info', self.name, message)

    def warning(self, message):
        self.make_logger_message('warning', self.name, message)

    def error(self, message):
        self.make_logger_message('error', self.name, message)

    def critical(self, message):
        self.make_logger_message('critical', self.name, message)
        sys.exit([0])


    def make_logger_message(self, level, name, message):
        msg = f'[{datetime.datetime.now()}] - {level} - [logger name >> {name}] - [{message}]'
        self.write_log(name, msg)