def hello():
    print('Hello!')

def user_age_seconds():
    user_age = int(input('Enter your age: '))
    age_seconds = user_age * 365 * 24 *60 * 60
    print(f'Your age in seconds: {age_seconds}')

user_age_seconds()

def add(x,y):
    result = x + y
    print(result)

def divide(dividend,divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print('You fool!')

def add(x, y=8):
    print(x + y)

def add(x,y):
    return x + y

#lambda functions
add = lambda x, y: x + y

(lambda x, y: x + y)(5,7)

sequence = [1, 3, 5, 9]
doubled = list(map(lambda x: x * 2, sequence))

#first class functions
def divide(dividend, divisor)
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)

#decorators
def get_admin_password():
    return '1234'

def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin'
            return func
    return secure_function
get_admin_password = make_secure(get_admin_password)


