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

# price = 1000000
# is_good = True
#
# if is_good:
#     price = price * 0.1
# else:
#     price = price * 0.2
# print(price)

# has_high_income = False
# has_good_credit = True
# has_criminal_record = False

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temperature  = 30
#
# if temperature <= 30:
#     print("It's a hot day")

# name = input("name: ")
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good!")

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# is_run = False
# while True:
#     order = input("> ").lower()
#     if order == 'help':
#         print('start - to start the car')
#         print('stop - to stop the car')
#         print('quit - to exit')
#     elif order == 'start':
#         if is_run == False:
#             print('Car statrted... Ready to go!')
#             is_run = True
#         else:
#             print('Car is already statrted')
#     elif order == 'stop':
#         if is_run == True:
#             print('Car stopped...')
#             is_run = False
#         else:
#             print('Car is already stopped.')
#     elif order == 'quit':
#         break
#     else:
#         print("I don't understand that...")

# for item in 'Python':
#     print(item)

# for item in [1,2,3,4]:
#     print(item)

# for item in range(5,10,2):
#     print(item)

# prices = [10, 20, 30]
# sum = 0
# for item in prices:
#     sum +=  item
# print(f"Total:{sum}")

# for循环
# for x in range(4):
#     # print(x)
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     # print('x'*num)
#     output = ''
#     for i in range(num):
#         output+='x'
#     print(output)

# 列表
# numbers = [5,2,1,5,7,4]
# numbers.append(20)
# numbers.insert(0,10)
# numbers.remove(5)
# # numbers.clear()
# numbers.pop()
# print(numbers)
# print(numbers.index(5))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.sort()
# print(numbers)
# print(numbers2)

# numbers = [2,2,3,4,3,4,6,1]
# for item in numbers:
#     if numbers.count(item)>1:
#         numbers.remove(item)
# print(numbers)

# 解压缩
# coordinates = (1,2,3)
# x,y,z = coordinates#元祖列表均可使用
# print(x)

# 字典
# costumer = {
#     "name":"dyl",
#     "age":30,
#     "is_verified":True
# }
# costumer["name"] = 'dyll'
# print(costumer["name"])
# print(costumer.get("birthdate","Jan 1 1980"))
# # 不会报错，没有会返回默认值

#字符串拆分,替换
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)":"😊",
#     ":(":"😒"
# }
# output = ''
# for word in words:
#     output += emojis.get(word,word)+" "
# print(output)

# 函数定义
# def greet_user(first_name,last_name):
# #     print(f"Hi {first_name} {last_name}!")
# #     print("Welcome aboard")
# #
# # print("Start")
# # greet_user("John","Smith")
# # greet_user(last_name="Mary",first_name="aaa")
# # print("Finish")

# def square(number):
#     return number * number
#
# # result = square(3)
# # print(result)
# print(square(3))

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)":"😊",
#         ":(":"😒"
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word,word)+" "
#     return output
# message = input("> ")
# output = emoji_converter(message)
# print(output)

# 异常处理
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0')
# except ValueError:
#     print('Invalid value')

# Class
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def mov(self):
#         print("move")
#
#     def draw(self):
#         print("draw")

# point1 = Point(10,20)
# point1.x = 11
# # point1.y = 20
# print(point1.x)
# # point1.draw()

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
# dyl = Person("dyl")
# dyl.talk()
#
# bob = Person("Bob")
# bob.talk()

# 继承
# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
#
# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.be_annoying()

# 模块
# import converters
# from converters import kg_to_lbs
#
# print(kg_to_lbs(100))
#
# print(converters.kg_to_lbs(70))
