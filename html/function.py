# def name_of_function():
#     some_code 
#     return variable 

# name_of_function()

# def function():
#     print('The function is called') 
#     return 'Makers' # return возвращает значение 

# print(function()) # Получим None птмчто функция не возвращает результат 


# def substract():
#     num1 = 20
#     num2 = 5 
#     print(num1 + num2)
#     return num1 - num2 

# # print(substract())

# # variable = substract()
# # print(variable) # Можно переменным присвоить функции 
 
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, substract()]
# print(list_)


# def substract():
#     num1 = 20
#     num2 = 5 
#     print(num1 + num2)
#     return num1 - num2 

# def function():
#     print("I'm calling substract functions")
#     variable = substract()
#     return variable

# print(function())

######################################################

# def multiply(a, b):
#     return a * b

# num1 = int(input('1:'))
# num2 = int(input('2:'))


# print(multiply(num1, num2))


# def welcome(name, last_name):
#     return f'Welcome, {name} {last_name}'

# a = input('Enter the name :')
# b = input('Enter the last name :')

# print(welcome(a, b))


#######################################################

# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     print(list_vowels)
#     result = ''.join(list_vowels)
#     return result


# a = input('Enter the word:')

# print(get_vowels(get_word(a)))

##############################################################

# def info(name, age):
#     return f'{name} is {age} years old'

# print(info(name='Sam', age=19)) # Именнованный аргумент 

###########################################################
# def test_func(n1, n2=9):
#     return n1 + n2 

# print(test_func(n1=9, n2=10))
#########################################################
# def create_profile(name, age, image='default'):
#     return name, age, image

# print(create_profile(name='Raimbek', age=17))

#########################################################
# *args **kwargs 

# def  func(reguired , *args, **kwargs):  # required обязательный параметр а  kwargs и args не обязательные
#     print(reguired)

#     if args: #True
#         print(args) # args создает кортеж от  позиционных аргументво 

#     if kwargs:
#         print(kwargs) # kwargs создает словарь от именнованых аргументов 
        
# func('makers', 'makers', key='value')


######################################################

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)

# many('raim', 'kello', hello='world')



#3


# dict_ = {
#     'Hello': 'World',
#     'Raimbek': 'Aidakeev',
#     'World': 'Hello'
# }

# def dictionary(a):
#     for i in a.keys():
#         print(i) 
    
# a = dict_ 
# dictionary(a)


########################################################
# def is_palindrome(word):
#     if word.lower() == word[::-1].lower():
#         return True 
#     else:
#         return False 
    
# print(is_palindrome('довод'))

#######################################################

# def multiply_list(list_):
#     sum_list = 0 
#     for i in list_:
#         sum_list = sum_list + i 
#     return sum_list 
    
# print(multiply_list([1, 2, 3, 4, 5, 6]))

########################################################

# def sum_digits(num):
    
#     sum =0
#     while (num != 0):
#         sum = sum + num % 10
#         num = num // 10 
#     return sum
    
# print(sum_digits(105))


# print(sum_digits(105))


# num = int(input("Введите целое: "))
# sum = 0
# while (num != 0):
#     sum = sum + num % 10
#     num = num // 10 
# print("Сумма цифр числа равна: ", sum)

###########################################################

# def func12(list_):
#     list_ = [x.lower() for x in list_]
#     return list_

# print(func12(['Hello', 'WOrLd']))
#########################################################
#Task1 
# import random 

# def generate_password(param1, param2):
#     random_list = random.sample(range(1, 10), k=7)
#     random_list = [str(i) for i in random_list]
#     password = param1 + param2 + ''.join(random_list)
#     return password


# def get_info(name=input('Ведите имя:'),
#             last_name=input('Ведите фамилию:')):
#     password = generate_password(param1=name, param2=last_name)
#     return password 

# print(get_info())

#Task2 (calculator on function)

# def add(a, b):
#     return a+b 

# def substract(a, b):
#     return a - b 

# def multiply(a, b):
#     return a * b 

# def division(a, b):
#     return a / b

# def result(param):
#     return param 

# def get_data(action):
#     num1 = int(input('Enter the first number:'))
#     num2 = int(input('Enter the second number:'))

#     dictionary = {'+': add(num1, num2),
#                   '-': substract(num1, num2),
#                   '*': multiply(num1, num2),
#                   '/': division(num1, num2),}
    
#     some_result = dictionary[action]
#     return result(some_result)

# action = input('Select action from list below: + - * / + \n')
# print(get_data(action))

###########################################################
#Task 3 

def make_icecream(name, size, **kwargs):
    print (f'Your {name} icecream {size} size')

    if kwargs:
        print('Your toppings:')
        for value in kwargs.values():
            print('\t' + value)
    
make_icecream(name='chocalate', size='medium',
              topping1='peanuts', topping2='cocunt')


