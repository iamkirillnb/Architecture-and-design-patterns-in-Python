import encodings
import json
from .models import Student, Courses, Categories


def api_students(request):
    students = Student.json()
    return '200 OK', students


def api_courses(request):
    courses = Courses.json()
    return '200 OK', courses


def api_categories(request):
    categories = Categories.json()
    return '200 OK', categories

