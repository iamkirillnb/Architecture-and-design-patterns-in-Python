from dataclasses import dataclass
from re import S
from pprint import pprint
from markupsafe import re
from app import NotFoundPage


def get(environ, routes, fronts, data):
    path = environ['PATH_INFO']
    if path in routes:
        if path == "/users" and environ['QUERY_STRING']:
            item = environ['QUERY_STRING']
            k, v = item.split('=')
            data.append({"name":v})
        controller = routes[path]
    else:
        controller = NotFoundPage()
    request = {}
    for front in fronts:
        front(request)
    answer, body = controller(request, data)
    return answer, body

def post(environ, routes, fronts, data):
    pprint(environ)
    answer, body = "200", "post method"
    return answer, b'post method'




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



def post(environ):
    body = get_wsgi_input_data(environ)
    result = parse_wsgi_input_data(body)
    answer, body = '200 OK', b'data sent successfully'
    return result, answer, body


class Application:
    def __init__(self, routes, fronts, data):
        self.routes = routes
        self.fronts = fronts
        self.data = data

        self.comments = []

    def __call__(self, environ, start_response):
        method = environ['REQUEST_METHOD']

        if method == "GET":
            answer, body = get(environ, self.routes, self.fronts, self.data)
            
        if method == "POST":
            if environ['PATH_INFO'] == "/contact":
                result, answer, body = post(environ)
                # here we will write data to DB
                self.comments.append(result)
        start_response(answer, [('Content-Type', 'text/html')])
        return [body]