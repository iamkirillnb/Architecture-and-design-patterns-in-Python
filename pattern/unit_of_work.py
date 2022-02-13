# import abc
# import threading
# from app.models import Student
#
# class MapperRegistry:
#     @staticmethod
#     def get_mapper(obj):
#         if isinstance(obj, Student):
#             return (connection)
#
# class UnitOfWork:
#     """
#     Паттерн UNIT OF WORK
#     """
#     # Работает с конкретным потоком
#     current = threading.local()
#
#     def __init__(self):
#         self.new_objects = []
#
#     def register_new(self, obj):
#         self.new_objects.append(obj)
#
#
#     def commit(self):
#         self.insert_new()
#
#     def insert_new(self):
#         for obj in self.new_objects:
#             MapperRegistry.get_mapper(obj).insert(obj)
#
#
#     @staticmethod
#     def new_current():
#         __class__.set_current(UnitOfWork())
#
#     @classmethod
#     def set_current(cls, unit_of_work):
#         cls.current.unit_of_work = unit_of_work
#
#     @classmethod
#     def get_current(cls):
#         return cls.current.unit_of_work
#
#
# class DomainObject(metaclass=abc.ABC):
#     def mark_new(self):
#         UnitOfWork.get_current().register_new(self)
