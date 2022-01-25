from dataclasses import dataclass
from re import S
from pprint import pprint
from markupsafe import re
from app import NotFoundPage





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