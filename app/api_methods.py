import encodings
import json
from .models import Student, Courses, Categories


def api_students(request):
    students = Student.all()
    return '200 OK', json.dumps(students, indent=2).encode('utf-8')


def api_courses(request):
    courses = Courses.all()
    return '200 OK', json.dumps(courses, indent=4).encode("UTF-8")


def api_categories(request):
    categories = Categories.all()
    return '200 OK', json.dumps(categories, indent=4).encode("UTF-8")

