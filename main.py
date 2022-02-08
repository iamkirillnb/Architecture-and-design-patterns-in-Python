
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
    '/students': app.student_page,
    '/students/create_student': app.create_student_page,
    '/courses/course':app.course_page,
    '/about': app.about_page,
    '/contact': app.contact_page
}



def secret_front(request):
    request['secret'] = 'some secret'

    
def other_front(request):
    request['key'] = 'value'


app_object = framework.Application(routes, [secret_front, other_front])
