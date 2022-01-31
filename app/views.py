from ast import arg
import framework
from pattern import log


def index_page(request, *args):
    log()
    output = framework.render(template_name="app/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')

def categories_page(request):
    log()
    if request['QUERY_STRING']:
            data = framework.parse_input_data(request['QUERY_STRING'])
            for k,v in data.items():
                dict.append({k:v})
    output = framework.render(template_name="app/categories.html", categories=request['categories'])  
    return '200 OK', output.encode('utf-8')

def category_page(request):
    log()
    output = framework.render(template_name="app/category.html", kwargs={})  
    return '200 OK', output.encode('utf-8')

def create_category_page(request):
    log()
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        if result['categorie_name'] != '':
            request['categories'].append(result)
    output = framework.render(template_name="app/create_category.html", courses=dict)  
    return '200 OK', output.encode('utf-8')

def courses_page(request):
    log()
    output = framework.render(template_name="app/courses.html", courses=request['courses'])  
    return '200 OK', output.encode('utf-8')

def course_page(request):
    log()
    output = framework.render(template_name="app/course.html", kwargs={})  
    return '200 OK', output.encode('utf-8')

def create_course_page(request):
    log()
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        if result['course_name'] != '':
            request['courses'].append(result)
    output = framework.render(template_name="app/create_course.html", courses=dict)  
    return '200 OK', output.encode('utf-8')

def about_page(request, *args):
    log()
    output = framework.render(template_name="app/about.html")
    return '200 OK', output.encode('utf-8')


def contact_page(request, *args):
    log()
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        print(result)
    output = framework.render(template_name="app/contact.html")
    return '200 OK', output.encode('utf-8')



