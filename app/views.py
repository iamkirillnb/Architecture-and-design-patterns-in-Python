from ast import arg
import framework
from pattern import debug
from pprint import pprint
import json
from .models import Student, Courses, Categories

log = framework.Logger('School_app')


@debug
def index_page(request):
    log.debug("index_page")
    output = framework.render(template_name="app/index.html", kwargs={"name": "user"})
    return '200 OK', output.encode('utf-8')


@debug
def categories_page(request):
    log.debug("categories_page")
    categories = Categories.all()
    output = framework.render(template_name="app/categories.html", categories=categories)
    return '200 OK', output.encode('utf-8')


@debug
def create_category_page(request):
    log.debug("create_category_page")
    if request['REQUEST_METHOD'] == 'POST':
        if request['post']["categorie_name"] != '':
            category = Categories(request['post']["categorie_name"])
            category.write_category()
        else:
            return '400', b'not valid data'
    output = framework.render(template_name="app/create_category.html", kwargs={})
    return '200 OK', output.encode('utf-8')


@debug
def courses_page(request):
    log.debug("courses_page")
    courses = Courses.all()
    output = framework.render(template_name="app/courses.html", courses=courses)
    return '200 OK', output.encode('utf-8')



@debug
def create_course_page(request):
    log.debug("create_course_page")
    categories = Categories.all()
    if request['REQUEST_METHOD'] == 'POST':
        if request['post']["course_name"] != '':
            course = Courses(request['post']["course_name"], request['post']["category_name"])
            course.write_course()
        else:
            return '400', b'not valid data'
    output = framework.render(template_name="app/create_course.html",
                              kwargs={'categories': categories})
    return '200 OK', output.encode('utf-8')


@debug
def student_page(request):
    log.debug("student_page")
    students = Student.all()
    output = framework.render(template_name="app/students.html", students=students)
    return '200 OK', output.encode('utf-8')


@debug
def create_student_page(request):
    log.debug("create_student_page")
    courses = Courses.all()
    if request['REQUEST_METHOD'] == 'POST':
        if request['post']["student_name"] != '' or request['post']["phone_number"] != '':
            student = Student(request['post']["student_name"], request['post']["phone_number"], request['post']["course_name"])
            student.write_student()
        else:
            return '400', b'not valid data'
    output = framework.render(template_name="app/create_student.html", kwargs={'courses': courses})
    return '200 OK', output.encode('utf-8')


@debug
def about_page(request):
    log.debug("about_page")
    output = framework.render(template_name="app/about.html")
    return '200 OK', output.encode('utf-8')


@debug
def contact_page(request):
    log.debug("contact_page")
    if request['REQUEST_METHOD'] == 'POST':
        body = framework.get_wsgi_input_data(request)
        result = framework.parse_wsgi_input_data(body)
        print(result)
    output = framework.render(template_name="app/contact.html")
    return '200 OK', output.encode('utf-8')
