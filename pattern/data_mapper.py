import abc
import sqlite3

from app.models import Student, Courses, Categories


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class SqliteStudentMapper():
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_all(self):
        statement = f"SELECT * FROM student"
        data = []
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            for r in result:
                data.append(Student(*r))
            return data
        else:
            return []

    def insert(self, student, phone, course):
        statement = f"INSERT INTO student (name, phone, course_id) VALUES (?, ?, ?)"
        self.cursor.execute(statement, (student, phone, course))
        self.connection.commit()

class SqliteCourseMapper():
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_all(self):
        statement = f"SELECT * FROM course"
        data = []
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            for r in result:
                data.append(Courses(*r))
            return data
        else:
            return []

    def insert(self, course_name, category_id):
        statement = f"INSERT INTO course (course_name, category_id) VALUES (?, ?)"
        self.cursor.execute(statement, (course_name, category_id))
        self.connection.commit()

class SqliteCategoryMapper():
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_all(self):
        statement = f"SELECT * FROM category"
        data = []
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            for r in result:
                data.append(Categories(*r))
            return data
        else:
            return []

    def insert(self, category_name):
        statement = f"INSERT INTO category (category_name) VALUES (?)"
        self.cursor.execute(statement, (category_name,))
        self.connection.commit()