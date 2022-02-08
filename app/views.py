from ast import arg
import framework
from pattern import debug, Logger
from pprint import pprint
import json

log = Logger('School app')
@debug
def index_page(request):
    log.logger.debug("index_page")
    output = framework.render(template_name="app/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')


@debug
def categories_page(request):
    log.logger.debug("categories_page")
    categories = framework.read_from_file("categories")
    output = framework.render(template_name="app/categories.html", categories=categories)
    return '200 OK', output.encode('utf-8')


@debug
def category_page(request):
    log.logger.debug("category_page")
    output = framework.render(template_name="app/category.html", categories=request['categories'])
    return '200 OK', output.encode('utf-8')


@debug
def create_category_page(request):
    log.logger.debug("create_category_page")
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        if result['categorie_name'] != '':
            framework.write_to_file("categories", result["categorie_name"])
    output = framework.render(template_name="app/create_category.html", kwargs={})
    return '200 OK', output.encode('utf-8')


@debug
def courses_page(request):
    log.logger.debug("courses_page")
    courses = framework.read_from_file("courses")
    output = framework.render(template_name="app/courses.html", courses=courses)
    return '200 OK', output.encode('utf-8')


@debug
def course_page(request):
    log.logger.debug("course_page")
    courses = framework.read_from_file("courses")
    output = framework.render(template_name="app/course.html", courses=courses)
    return '200 OK', output.encode('utf-8')


@debug
def create_course_page(request):
    log.logger.debug("create_course_page")
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        if result['course_name'] != '':

            framework.write_to_file("courses", result["course_name"])
    output = framework.render(template_name="app/create_course.html", kwargs={})
    return '200 OK', output.encode('utf-8')


@debug
def student_page(request):
    log.logger.debug("student_page")
    students = framework.read_from_file("students")
    output = framework.render(template_name="app/students.html", students=students)
    return '200 OK', output.encode('utf-8')


@debug
def create_student_page(request):
    log.logger.debug("create_student_page")
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        if result['student_name'] != '':
            framework.write_to_file("students", result["student_name"])
    output = framework.render(template_name="app/create_student.html", kwargs={})
    return '200 OK', output.encode('utf-8')


@debug
def about_page(request):
    log.logger.debug("about_page")
    output = framework.render(template_name="app/about.html")
    return '200 OK', output.encode('utf-8')


@debug
def contact_page(request):
    log.logger.debug("contact_page")
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        print(result)
    output = framework.render(template_name="app/contact.html")
    return '200 OK', output.encode('utf-8')

