
import string
import app
import framework
import io



routes = {
    "/": app.index_page,
    "/users": app.users_page,
    "/about": app.about_page,
    "/contact": app.contact_page
}

data = [
    {"name": "kirill"},
    {"name": "Olga"},
    {"name": "Nikita"},
    {"name": "Angelina"},
]

def secret_front(request):
    request['secret'] = 'some secret'

    
def other_front(request):
    request['key'] = 'value'




app_object = framework.Application(routes, [secret_front, other_front], data)
