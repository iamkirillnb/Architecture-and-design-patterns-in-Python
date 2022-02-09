import json
from dataclasses import dataclass
from re import S
from pprint import pprint

from urllib import request
from markupsafe import re

from .render import render as renderTemp


def add(argument):
    def decorator(function):
        def wrapper(req):
            req['PATH_INFO'] = argument

            result = function(req)

            return result

        return wrapper

    return decorator


def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    # получаем длину тела
    content_length_data = env.get('CONTENT_LENGTH')
    # приводим к int
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные, если они есть

    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        # собираем их в словарь
        result = parse_input_data(data_str)
    return result


class NotFoundPage:
    def __call__(self, request, *args):
        output = renderTemp(template_name="error.html")
        return '200 OK', output.encode('utf-8')


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

        self.comments = []

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        for k, v in self.routes.items():
            if path in v:
                controller = v[path]
            else:
                controller = NotFoundPage()
        for front in self.fronts:
            front(environ)
        answer, body = controller(environ)
        start_response(answer, [('Content-Type', 'text/html')])
        return [body]


def write_to_file(key, data):
    with open("data.json", "r", encoding="UTF-8") as file:
        data_bd = json.loads(file.read())
        data_bd[key].append(data)
    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(data_bd, file, indent=2, ensure_ascii=False)
    return


def read_from_file(name):
    response = []
    with open("data.json", "r", encoding="UTF-8") as file:
        data = json.loads(file.read())
        for d in data[name]:
            response.append(d)
    return response
