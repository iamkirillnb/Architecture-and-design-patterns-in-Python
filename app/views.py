from re import A
import app

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


def index_page(request, *args):
    output = app.render(template_name="./templates/app/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')

def users_page(request, dict):
    output = app.render(template_name="./templates/app/users.html", users=dict)  
    return '200 OK', output.encode('utf-8')


def about_page(request, *args):
    output = app.render(template_name="./templates/app/about.html")
    return '200 OK', output.encode('utf-8')


def contact_page(request, *args):
    if request['method'] == 'POST':
        body = get_wsgi_input_data(request['env'])
        result = parse_wsgi_input_data(body)
        print(result)
    output = app.render(template_name="./templates/app/contact.html")
    return '200 OK', output.encode('utf-8')


class NotFoundPage:
    def __call__(self, request, *args):
        output = app.render(template_name="./templates/app/error.html")
        return '200 OK', output.encode('utf-8')
