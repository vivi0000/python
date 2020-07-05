# print("dyl")
# print('*' * 10)
# * 10：做10次

# price = 10
# rating = 4.9
# name = 'DYL'
# is_published = False
# print(price)

# name = input('What is your name? ')
# print('Hi '+name)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# #input返回str
# age = 2019 - int(birth_year)
# # int()
# # bool()
# # float()
# print(type(age))
# print(age)

# course = "Python's Course for Beginners"
# course = 'Python for "Beginners"'
# course = """"
# Hi Jhon,
#
# Here is our first email to you.
#
# Thank you
# """
# print(course)

# course = 'Python for Beginners'
# print(course[0])#P
# print(course[-1])#s
# print(course[0:3])#Pyt
# print(course[0:])#Python for Beginners
# print(course[1:])#ython for Beginners
# print(course[:5])#Pytho
# another = course[:]#Python for Beginners
# print(another)

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# #John [Smith] is a coder
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find('P'))
# print(course.find('Beginner'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print('python' in course)
# print(course)

# print(10/3)     #3.3333333333333335
# print(10//3)    #3
# print(10%3)     #1
# print(10**3)    #1000

# x = 10
# x = x + 3
# x += 3
# print(x)

# x = 10 + 3 * 2 ** 2
# print(x)

# x = 2.9
# print(round(x))
# print(abs(-2.9))

# import math
#
# print(math.ceil(2.9))
# print(math.floor(2.9))

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

price = 1000000
is_good = True

if is_good:
    price = price * 0.1
else:
    price = price * 0.2
print(price)