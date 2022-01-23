
import string
import app
import framework
import io



routes = {
    "/": app.index_page,
    "/about": app.about_page,
    "/contact": app.contact_page
}

def secret_front(request):
    request['secret'] = 'some secret'

    
def other_front(request):
    request['key'] = 'value'




app_object = framework.Application(routes, [secret_front, other_front])
