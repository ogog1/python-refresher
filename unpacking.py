#unpacking argument
def multiply(*args):
    print(args)
    total = 1
    for arg in arg:
        total = total * arg
    return total

def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return 'No valid operator provided.'

#unpacking keyword arguments

def named(**kwargs):
    print(kwargs)

named(name='Bob', age=25)

def print_nicely(**kwargs)
    named(**kwargs)
    for arg,value in kwargs.items():
        print(f'{args:{value}')



