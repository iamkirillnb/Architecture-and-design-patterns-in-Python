from .views import *
from app.api_methods import api_courses, api_students, api_categories

routes = {
    "/app/": index_page,
    '/app/categories': categories_page,
    '/app/categories/create_category': create_category_page,
    '/app/categories/category': category_page,
    '/app/courses': courses_page,
    '/app/courses/create_course': create_course_page,
    '/app/students': student_page,
    '/app/students/create_student': create_student_page,
    '/app/courses/course': course_page,
    '/app/about': about_page,
    '/app/contact': contact_page,
    '/app/api/courses': api_courses,
    '/app/api/students': api_students,
    '/app/api/categories': api_categories
}
