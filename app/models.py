import sqlite3
import abc
import pattern
# from pattern import DomainObject


connection = sqlite3.connect('project.sqlite')


class Student:
    def __init__(self, name=None, phone=None, course=None):
        self.name = name
        self.phone = phone
        self.course = course

    def write_student(self):
        person_mapper = pattern.SqliteStudentMapper(connection)
        person_mapper.insert(self.name, self.phone, self.course)

    @staticmethod
    def all():
        person_mapper = pattern.SqliteStudentMapper(connection)
        return person_mapper.get_all()


class Categories:
    def __init__(self, category):
        self.category = category

    def write_category(self):
        category_mapper = pattern.SqliteCategoryMapper(connection)
        category_mapper.insert(self.category)

    @staticmethod
    def all():
        category_mapper = pattern.SqliteCategoryMapper(connection)
        return category_mapper.get_all()


class Courses:
    def __init__(self, course, category=None):
        self.course = course
        self.category = category

    def write_course(self):
        course_mapper = pattern.SqliteCourseMapper(connection)
        course_mapper.insert(self.course, self.category)

    @staticmethod
    def all():
        course_mapper = pattern.SqliteCourseMapper(connection)
        return course_mapper.get_all()
