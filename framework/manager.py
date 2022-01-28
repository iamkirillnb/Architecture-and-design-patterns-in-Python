from dataclasses import dataclass
from re import S
from pprint import pprint
from markupsafe import re
from .render import render as renderTemp





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
    def __init__(self, routes, fronts, data):
        self.routes = routes
        self.fronts = fronts
        self.data = data

        self.comments = []

    def __call__(self, environ, start_response):
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        query = environ['QUERY_STRING']
        request = {}
        request['method'] = method
        request['path'] = path
        request['query'] = query
        request['env'] = environ
        if path in self.routes:
            controller = self.routes[path]
        else:
            controller = NotFoundPage()
        for front in self.fronts:
            front(request)
        if query:
            data = parse_input_data(query)
            for k,v in data.items():
                self.data.append({k:v})
        answer, body = controller(request, self.data)
        start_response(answer, [('Content-Type', 'text/html')])
        return [body]