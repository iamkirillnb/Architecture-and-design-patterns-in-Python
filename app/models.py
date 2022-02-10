from abc import abstractmethod
from framework import write_to_file, read_from_file


class Student:
    def __init__(self, name, course=None):
        self.name = name
        self.course = course

    def write_student(self):
        write_to_file('students', {'name': self.name, 'courses': self.course})
        return

    @staticmethod
    def all():
        data = read_from_file('students')
        return data


class Categories:
    def __init__(self, category):
        self.category = category

    def write_category(self):
        write_to_file('categories', {'category': self.category})
        return

    @staticmethod
    def all():
        data = read_from_file('categories')
        return data

class Courses:
    def __init__(self, course, category=None):
        self.course = course
        self.category = category

    def write_course(self):
        write_to_file('courses', {'course': self.course, 'category': self.category})
        return

    @staticmethod
    def all():
        data = read_from_file('courses')
        return data