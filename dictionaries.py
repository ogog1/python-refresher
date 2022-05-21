friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27}

friend_ages['Adam']
friend_ages['Bob'] = 20
friend_ages['Adam'] = 25

friends = [
    {'name': 'Rolf', 'age':24 },
    {'name': 'Adam', 'age':25 },
    {'name': 'Anne', 'age':27 }
]

student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}')

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

#dict comprehensions

users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'bob123'),
    (2, 'Jose', 'longp4assword'),
    (3, 'username', '1234')
]

username_mapping = {user[1]: user for user in users}


