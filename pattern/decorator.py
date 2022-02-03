from cmath import inf
import datetime
import traceback


def debug(function):
    def wrapper(req):
        info = f'[{datetime.datetime.now()}] [function: {function.__name__}]'
        print(info)
        result = function(req)
        return result
    return wrapper