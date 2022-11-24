# print()   # Втроенные функции
# input()
# int()
# str()
# list()
# dict()
# frozenset()
# set()
# len()
# sum()
# bool()
# min()
# max()
# sorted()


# map(func, iterable object)

# list_str = ['1', '2', '3', '4']
# # list_int = []

# # for i in list_str:
# #     list_int.append(int(i))

# # print(list_int)

# list_int = list(map(int, list_str))
# print(list_int)

# def capital(word: str) -> str: # Анотация типов
#     return word.title()

# list_names = ['john', 'alice', 'raychel', 'sam']
# new_list = list(map(capital, list_names))
# print(new_list)

#############################################################

# def dollars_to_soms(dollars: int) -> int:
#     return f'{round(dollars * 84.80)} soms'

# dollars = [100, 50, 90, 65]

# soms = list(map(dollars_to_soms, dollars))
# print(soms)
#####################################################

#lamda( анонимная функция ) не поддерживает ретерн анотауцю функции

# print((lambda x: x ** 2) (46))

# square = lambda x: x ** 2
# print(square(46))

#############################################################

# print((lambda x, y, z: x + y + z)(1, 2,3))

###########################################################

# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [7, 8, 9]

# new_list = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
# print(new_list)

############################################################
# # loop
# num_list = [2, 6, 8, 7, 9, 1, 4]
# num_list2 = []
# for i in num_list:
#     num_list2.append(i * 2)

# print(num_list2)

# list copmrehension 
# num_list2  = [x * 2 for x in num_list]
# print(num_list2)

# map + lambda 
# num_list2 = list(map(lambda i: i * 2, num_list))
# print(num_list2)

#########################################################
# filter 

# names = ['john', 'alice', 'amber', 'raychel', 'sam', 'arnold']
# filtered_names = list(filter(lambda name: name.startswith('a'), names))
# print(filtered_names)

##########################################################
# numbers = [4, 5, 6, 2, 8, 9, 11, 12, 15, 17, 18]
# filtered_numbers = list(filter(lambda num: num % 3 == 0, numbers))
# print(filtered_numbers)


# dict1 = [{'subject': 'python', 'point': 89},
#          {'subject': 'javasript', 'pont': 92}]
# dict_new = list(filter(lambda x: x['subject'] == 'python', dict1))
# print(dict_new)


# users = [{'username': 'Alice123', 'comments': ['I love it', 'Good!!!']},
#          {'username': 'Sam', 'comments': []},
#          {'username': 'John', 'comments': []},
#          {'username': 'Raychel', 'comments': ['I like it !!!!!!!!!!']}]

# active_users = list(filter(lambda x: x['comments'], users))
# inactive_users = list(filter(lambda x: not x.get('comments', None), users))

# print(inactive_users)
# print(active_users)


# names = ['Alice', 'Sandra', 'Molly', 'Tim']
# greetings = list(map(lambda name: f'Welcome, {name}', filter(lambda x: len(x) >= 5, names)))
# print(greetings)

############################################################
# reduce(func, iterable object)

# import functools
# numbers = [1, 2, 3, 4]
# sum_ = functools.reduce(lambda x, y: x + y, numbers)
# print(sum_)


# numbers = [78, 56, 2, -9, 0, 3452, 6754, 2, 356]
# max_ = functools.reduce(lambda a, b: a if a > b else b, numbers)
# print(max_)



# from functools import reduce  
# numbers = [5, 6, 8, 1, 2]
# multiply = reduce(lambda x, y: x * y, numbers)
# print(multiply)

#########################################################

# zip()

# list_a  = [1, 2, 3, 4, 5]
# list_b = ['a', 'b', 'c', 'd', 'e']
# list_c = ['makers', 'bootcamp', 'hello', 'world', 'zip']

# zipped_list = list(zip(list_a, list_b, list_c))
# list_numbers, list_letters, list_str= list(zip(*zipped_list))
# print(list_numbers)
# print(list_letters)
# print(list_str)
# print(zipped_list)

# print(dir(__builtins__))

##########################################################
# enumerate()

# seasons = ['spring', 'winter', 'fall', 'summer']
# enumerate_seasons = list(enumerate(seasons, start=-1))
# print(enumerate_seasons)

###############################################################

#abs 
# negative = -123
# absolute = abs(negative)
# print(absolute)


#all

# list_of_zeros = [0, 0, 0, 0]
# is_true = all(list_of_zeros)
# print(is_true)

#any 

# list_of_zeros = [0, 0, 0, 1] # Если есть одно истина возвращает иснтину а all проверяет что бы все было тру
# is_true = any(list_of_zeros)
# print(is_true)


# ascii

# list_1 = ['makers', 'мэйкерс', 23, 0, '$']
# list_2 = ascii(list_1)
# print(list_2)



# ord()
# chr()

# print(ord('1')) #only sstr unicode
# print(chr(69))


# divmod()
# a = 15
# b = 7
# print(divmod(a, b)) # возвращает 2 числа 1 целое 2 остаток

#############################################################
#############################################################
# from functools import reduce 

# list_ = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, list_)
# print(result)


# list_ = [1, 2, 3, 4, 5]
# result = any([x < 0 for x in list_])
# print(result)

# list_ = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x**2, list_))
# print(result)


# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x%2==0, list_))
# print(result)


# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x)>7, list_))
# print(result)

# from functools import reduce

# list_ = [5, 6, 7, 8]
# result = reduce(lambda x, y: x*y, list_)
# print(result)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_1 = list(filter(lambda x: x%2==0, list_))
# list_2 = list(filter(lambda x: x%2!=0, list_))
# result = f'even: {len(list_2)}, odd:{len(list_2)}'
# print(result)

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: True if x > 0 else False , list_))
# print(result)

# import functools
# names = ['Raim', 'Litvin', 'John', 'Igor', 'Isken']
# result = functools.reduce(lambda x, y: x if len(x)> len(y) else y, names)
# print(result)


# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = functools.reduce(lambda x,y: x if len(x)>len(y) else y, list_)
# print(result)

# result = list(map(lambda x: 'Fizz' if x%3==0 else 'Buzz', range(1, 51)))
# print(result)

# from functools import reduce

# list_ = [2, 3, 4, 5, -1]
# result = reduce(min, list_)
# print(result)

# string = 'hello'
# print(tuple(enumerate(string)))

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# print(list(map(lambda x: abs(x), list_)))

# list_ = ['hello', 123]
# print(list(map(lambda x: type(x), list_)))


# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# print(list(map(lambda x: x + ' Python' if len(x)>5 else x + ' JavaScript', names)))


# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# list1 = list(filter(lambda x: x > 0, list_))
# list2 = list(filter(lambda x: x<0, list_))
# print(list(zip(list1, list2)))


list_ = ['a', 'n', 'n', 'a']
