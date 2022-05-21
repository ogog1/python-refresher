class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

#magic methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person {self.name}, {self.age} years old.'

    def __repr__(self):
        return f'<Person ({self.name}, {self.age})>'

#@classmethod @staticmethod
class ClassTest
    def instance_method(self):
        print(f'Called instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')

    @staticmethod
    def static_method():
        print('Called static_method.')

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_typy, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, weighs {self.weight} g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

#class inheritance
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} ({self.commected_by})'

    def disconnect(self):
        self.connected = False
        print('Disconnected.')

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining.)'

    def print(self, pages):
        if not self.connected:
            print('Your printer is not connected!')
            return
        print(f'Printing {pages} pages.')
        self.remaining_pages -= pages

#class composition
class BookShelf:
    def __init__(self, *books):
        self.books = quantity

    def __str__(self):
        return f'BookShelf with {len(self.books)} books.'

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'



