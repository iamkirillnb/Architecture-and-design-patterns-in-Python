
import string
import app
import framework
import io


routes = {
    "/": app.index_page,
    '/categories': app.categories_page,
    '/categories/create_category': app.create_category_page,
    '/categories/category':app.category_page,
    '/courses': app.courses_page,
    '/courses/create_course': app.create_course_page,
    '/courses/course':app.course_page,
    '/about': app.about_page,
    '/contact': app.contact_page
}

categories = [
    {"categorie_name": "Interpreted"},
    {"categorie_name": "Сompiled"},
]

courses = [
    {"categorie_name": "Interpreted", "course_name": "Python"},
    {"categorie_name": "Сompiled", "course_name": "Golang"},
    {"categorie_name": "Interpreted", "course_name": "Java Script"},
]

def secret_front(request):
    request['secret'] = 'some secret'

    
def other_front(request):
    request['key'] = 'value'


app_object = framework.Application(routes, [secret_front, other_front], courses, categories)
