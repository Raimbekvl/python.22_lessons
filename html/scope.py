# built-ins - встроенный пространства имен 
# global - глобальная пространства име 
# local - замкнутая пространства имен
# enclosed - вложенная пространства имен
# local - локальная пространства имен


# this_var_is_visible = 'You can see me inside and outside the function'

# def var_visibility():
#     this_var_is_not_visible = 'You can see me only inside the function'
#     print(this_var_is_not_visible )


# var_visibility()
# print(this_var_is_visible)
# print(this_var_is_not_visible) # Он его не видит птмчто принт ищет его в глобальном уровне 

##########################################################
# built-ins 
# print(dir(__builtins__)) # Встроенные ообьекты 
# name = 'Makers'
# name = 'Bootcamp'
# print(name)

##########################################################

# word = "I'm gllobal"

# def func_a():
#     # word = "I'm local"
#     print(word)

# func_a()
# print(word)

#########################################################

# word = "I'm global"

# def outer():
#     word = "I'm enclosed"
#     print(word)

#     def inner():
#         word = "I'm local"
#         print(word)
    
#     inner()

# outer()
# print(word)


########################################################
#globals(), locals()

# dict_ = {'name': 'Makers', 'name': 'Bootcamp'}
# print(dict_)

# name = 'Makers'
# name = 'Bootcamp'
# print(globals()) # Возвращает словрь глобального пространтсва имени
############################################################
# locals()

# def func():
#     name = 'Bootcamp'
#     name = 'Makers'
#     print(locals())

# func() # Возвращает те обьекты которые находятся в локальном пространстве в виде словаря


# def func(company):
#     name = 'Bootcamp'
#     print(locals())

# func(company='Makers')

###########################################################

# def info(name, age, heigh):
#     name = 'Alice'
#     age = 30 
#     print(locals())

# info(name='Carly', age=25, heigh=165)

# print(locals())
# print(globals())
 
# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
     
#     def bar():
#         global var
#         var = 'переменная bar'
        
#     bar()
# foo()
# print('переменная в foo: ', var)

# x = 'Я глобальная переменная'

# def val():
#     global x 
#     print('Я могу изменяться')

# print(x)
# val()

# num = 3 

# def multiply():
#     global num 
#     num = num * num 
#     num = num * num 

# multiply()
# print(num)

#########################################################


# balance = 0 

# def get_salary(amount):
#     global balance 
#     balance += amount

# def pay_bills (amount, log_name):
#     global balance 
#     balance -= amount 
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'internet')
# get_balance()

##########################################################

# result = 0 
# def pow_first (x, y):
#     global result 
#     result = x**y 

# def pow_second (z):
#     global result 
#     result %= z 

# pow_first(2, 3)
# pow_second(3)
# print(result)


#########################################################

# quest = {'Мурат': 24,
#                'Эржан': 21,
#                'Чынгыз': 24,
#                'Алтынай': 17,
#                'Асема': 16}



# def age_control():
#     global  ques
#     for name, age in quest.items():
#         if age < 18:
#             print(f'Sorry {name} ваш возраст {age}')
#         else:
#             print(f'Welcome to night clube {name}')


# age_control()

###############################################################

# name = ['raimbek', 'igor', 'sardar', 'john']

# new_name = []

# def func():
#     global name
#     global new_name
#     new_name = [x.title() for x in name]
#     print(new_name)

# func()

#########################################################


# def func_str(str_):
#     vowels = 0 
#     consonants = 0 
#     sumbols = 0 

#     for i in str_.lower():
#         if i in 'йуеыаоэяиюё':
#             vowels += 1 
#         elif i in "цкнгшщзмчвфжрлдтсп":
#             consonants += 1
#         else: 
#             sumbols += 1 
#     return f'Гласные: {vowels}, Согласные: {consonants}, Симболы:{sumbols}' 

# print(func_str('Мэйкерс буткемп !!!'))

#########################################################

# number = []

# def nums():
#     global number 
#     number = [x for x in range(11)]
#     return number

# print(nums())
############################################################

# list_ = []

# def num():
#     global list_ 
#     list_ = [x for x in range(30) if x < 7]
#     return list_ 

# print(num())

# size_global_matryoshka = 10 

# def matryoshka_2():

#     size_matryoshka_2 = 5 

#     def matryoshka_3():
#         size_matryoshka_3 = 3

#         return size_matryoshka_3 + size_matryoshka_2 

#     return matryoshka_3() + size_global_matryoshka
# print(matryoshka_2())

##############################################
# from random import choice
 
# def add():
#     global c
#     c.append(input('Введите имя '))
 
# def remove():
#     global c
#     if not len(c): return
#     del c[int(input(f'Удалить имя от 0 до {len(c) - 1} '))]
 
# c = []
# for i in range(10):
#     choice([add, remove])()
# print(c)
#####################################
# def irina(num=int(input('Ведите число месяцa:'))):
#     if num  > 12:
#         print('Такого месяца не существует !!! ')
#     elif num % 2 == 0:
#         return 'Красный'
#     else:
#         return'Черный'

# print(irina())
    
############################################################

# a = int(input())
# b = int(input())
# if a%b == 0:
#     print("%d делится на %d" % (a,b))
# else:
#     print("%d не делится на %d" % (a,b))
#     print("Остаток: %d" % (a%b))
# print("Частное: %d" % (a//b))
#############################################################

# num = [1, 2, 3, 4, 5, 6, 7, 8]

# def func():
#     global num 
#     new_num = [x**2 for x in num ]
#     return new_num

# print(func())
###########################################################


# num = 1 

# def factorial(n):
#     global num
#     for i in range(2, n+1):
#         num *= i 
#     return num 

# n = int(input('Num:'))
# print(factorial(n))