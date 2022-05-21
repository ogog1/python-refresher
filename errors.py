def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError('Dividor cannot be 0.')

    return dividend / divisor

grade = []

print('Welcome to the average grade program')
try:
    average = divide(sum(grades), len(grades))
    print(f'The average grade is {average}.')
except ZeroDivisionError as e:
    print(e)
    print('There are no grades in your list.')

#custom error classes
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
    f'<Book {self.name, read {self.pages_read} out of {self.page_count}.>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesError(
                f'<You tried to read {self.pages_read + pages} pages,
                but this book only has {self.page_count} pages.'
            )
        self.pages_read += pages
        print(f'You have now read {self.pages_read} out of {self.page_count}.')