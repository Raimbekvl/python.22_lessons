# dict_ = {}
# print(type(dict_))



# my_dict = {'name': 'Sam', 'Last_name': 'white', 'age': 23}
# print(my_dict)


# my_dict = dict(a=1, b=2, c=3)
# print(my_dict)
# my_dict2 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
# }
# print(my_dict2)

#Превращение списка в словарь 

# my_list = [['m',1], ['a', 2], ['k',3]]
# my_dict = dict(my_list)
# print(my_dict)


# dict_ = {1: 'Makers', '2': True, False: []}
# print(dict_)


# Python 3.6 упорядочный 

# dict_ = {1:'Makers', '2': True, False:[]}
#Order Dict 





# dict_ = {
#     'Thom': 'black',
#     'Aice': 'yellow',
#     'Sam':  'green',}

# # print(dict_['Aice'])
# dict_['Alice'] = 'pink'
# dict_['Raychel'] = 'blue' #На ходу можно создавать 
# print(dict_)


#Методы словарей

#get(key, None)
# my_dict = {
#     1: 'Thom',
#     2: 'John',
#     3: 'Alice'} 

# print(my_dict.get(4, 'no such key in my dict')) #Значение по ключу отличие None
# print(my_dict[3])
# print(my_dict)


# clear() 
# my_dict = {
#     1: 'Thom',
#     2: 'John',
#     3: 'Alice'} 
# print(my_dict.clear())


#copy()

# my_dict = {
#     1: 'Thom',
#     2: 'John',
#     3: 'Alice'} 
# my_dict2 = my_dict.copy()

# my_dict[2] = 'Raychel'
# print(my_dict)
# print(my_dict2)

#pop(key, default)
# dict_ = {
#     'name': 'Kate',
#     'height': 170,
#     'weight': 50
# }

# dict_.pop('weight')
# print(dict_)


#popitem() - рандомно  может удалить пару ключ значения, усли ничего не передавать удаляет последний элемент словаря

# dict_ = {
#     'name': 'Kate',
#     'height': 170,
#     'weight': 50
# }
# dict_.popitem()
# print(dict_)

# setdefault()  - возвращает значение ключа, если нет то создает ключ 
# dict_ = dict(
#     a = 1,
#     b = 2,
#     c = 3)
# print(dict_.setdefault('d', 5))
# print(dict_)



# update() -  расширяет словарь за счте другого 

# dict1 = {
#     1: 'Tom',
#     2: 'Alice'}
# dict2 = {
#     3: 'Bob',
#     4: 'Ann'}
# dict1.update(dict2)
# print(dict1)
# print(dict2)


# fromkeys(seq, value) - создает словарь со значеением
# numbers = [1, 2, 3, 4, 5]
# new_dict = dict.fromkeys(numbers, 'Makers')
# print(new_dict)

# items(), keys(), values()

# dict_ = {
#     'name': 'Kate',
#     'height': 170,
#     'weight': 50
# }
# print(dict_.items())
# print(dict_.keys())
# print(dict_.values())

# contacts = {
#     'Alice': '+996552104557',
#     'John': '+996552630063',
#     'Sam': '+996552104557'}

# for name, tel in contacts.items():
#     print(f'Name: {name}, Tel:{tel}')
# for key in contacts.keys():
#     print(key)
# for value in contacts.values():
#     print(value)



# a = {'a': 1, 'b': 2, 'c': 1}
# a['f'] = 55
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)



# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys()))


# a = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# b = a.copy()
# print(b)

# a = {'a': 1, 'b': 2, 'c': 1}

# for keys in a.values():
#     print(keys)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for i,v in a.items() :
#   if v %2 ==0 :
#       b[i] = 2
#   else:
#       b[i]= v
# print(b)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for g, v in list(a.items()):
#     if v == None:
#         a.pop(g)

# print(a)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 

# for k, v in a.items():
#     a[k] = v/5
# print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10} 

# for k,v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)

# print(a)

a = {'a': 1, 'b': 2, 'c': 3} 

for k, v in list(a.items()):
    del a[k] 
    a[v] = k
print(a)