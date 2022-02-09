
import string
import app
import framework
import io
from app.urls import routes

urls = {
    "app/": routes,
}



def secret_front(request):
    request['secret'] = 'some secret'

    
def other_front(request):
    request['key'] = 'value'


app_object = framework.Application(urls, [secret_front, other_front])
