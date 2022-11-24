# numbers1 = []
# numbers2 = list()

# print(type(numbers1))
# print(type(numbers2))

# numbers4 = [1, 2, 3, 4]
# numbers5 = [numbers4]
# print(type(numbers5))
# print(type(numbers4))

# numbers = [7, 7, 7, 7, 7, 7]
# numbers2 = [7] * 6
# print(numbers)
# print(numbers2)

# range 
# 1. range(end)
# numbers = list(range(10)) ->  0 - 9
# print(numbers)

# 2. range(start, end)
# numbers = list(range(1,20)) -> 1-19
# print(numbers)

# 3. range(start, end, step)
# numbers = list(range(1, 20, 2)) -> 1-19 with step 2
# print(numbers)

# numbers = list(range(10, 0, -1)) -> от большего к меньшему шаг должен быть отрицательным если мы хотим в обратном порядке
# print(numbers)

# for i in range(1, 11):
#     print(i ** 2) 

#Сравнение 
# numbers1 = [1, 2, 3, 4, 5, 11] -> Сравнивает по индексу с начала 
# numbers2 = [1, 2, 3, 4, 5, 9, 100]

# print(numbers1 > numbers2)




# numbers = [1, True, 'Makers', 'hello', 8.9, (1, 2), ['hello']]
# print(numbers)


# Индексация 
# numbers = [1, True, 'Makers', 'hello', 8.9, (1, 2), ['hello']]
# print(numbers[7])


# print(numbers[0])
# print(numbers[2])
# print(numbers[4])
# print(numbers[-1])
# print(numbers[-2])

# numbers = [1, True, 'Makers', 'hello', 8.9, (1, 2), ['hello']] - Лист изменямые
# print(numbers)
# numbers[3] = 'bootcamp'
# numbers[-1] = {'hello': 'Monkey'}
# print(numbers)


# string = 'Makers' - Строки неизменяемые
# string[-1] = 'S'
# print(string)

# users = ['Alice', 'Sam', 'Carly']

# for i in users:
#     print(f'Hello {i} !')

# for letter in 'Makers':
#     print(letter.upper())

# Методы списков 

#append() - Добавляет элемент в конец списка 
# users = ['Alice', 'Cat', 'Billy']
# print(users)  #без имзенений 
# user = 'Tom'
# users.append(user)
# print(users) #Добавился элемент
# print(users[-1])


# guests = []
# list_length = int(input('Enter number of guests:'))

# for i in range(list_length):
#     guest = input('Enter guest name:')
#     guests.append(guest)

# print(guests)





#extend(list) - Расширяет список 

# users1 = ['Alice', 'Sam']
# users2 = ['Bob', 'Thom']
# users1.extend(users2)
# print(users1)
# print(users2)

# users2.extend(['John', 'Aibek'])
# print(users2)

# print(users1 + users2)

# insert() - добавляет элемент в список по индексу 
 
# users = ['John', 'Lenny', 'Andy', 'Ann']
# users.insert(1, 'Raychel')
# print(users)

# remove() удаляет элемент и только первое вхождение 
# users = ['Sam', 'Cat', 'Carly', 'Cat']
# users.remove('Cat')
# print(users)



#clear()

# users = ['Sam', 'Cat', 'User']
# print(users)
# users.clear()
# print(users)


# del users - Полностью удаляет из память 
# print(users)

#index(element) - Возвращает индекс элемента

# my_list = ['hello', 'makers', True, 6]
# print(my_list.index('makers'))
# print(my_list)

#pop(index) - удаляет элемент и возвращает если не передан индекс удаляет последний элемент

# numbers = [1, 2, 3, 4, 5]
# number = numbers.pop(1)
# number2 = numbers.pop()


# print(numbers)
# print(number2)

#count(element) - возвращает количество вхождений этого элемента в список
# numbers = [2, 4, 2, 2, 6, 7,8,2,2,2]

# print(numbers.count(2))

# sort(key) сортирует элементы

# users = ['Alice', 'Thomas', 'Cat', 'Ann', 'Raychel']
# users.sort(key=len)
# print(users)



#revesre() - переворачивает элементы в обратном порядке

# users = ['Alice', 'Thomas', 'Cat', 'Ann', 'Raychel']
# users.reverse()
# print(users)


#copy() - копирует список 

# users1 = ['Tom', 'Bob', 'Ann']
# users2 = users1.copy()
# print(id(users1))
# print(id(users2))
# users1.pop()
# print(users1)
# print(users2)


# Functions 

# len()
# numbers = [1, 2, 3, 4, 6, 8, 0, -1, -5]
# print(len(numbers))

# max(), min()

# numbers = [4, 1, 6, 8, 9, 0]
# print(max(numbers))
# print(min(numbers))


# sum()

# numbers = [4, 1, 6, 8, 9, 0]
# print(sum(numbers))

#sorted()

# numbers = [5, 1, 9, 3, 4, 6]
# print(sorted(numbers))

#Срезы

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list[x:y] - от икса до игрика не включительно 
# print(my_list[1:4])
# my_list = my_list[1:4]
# print(my_list)
# list[x:y:z]
# print(my_list[2:-1:2])


# users = [
#     ['Tom', 23],
#     ['Bob', 34],
#     ['Emily', 19]
# ]

# print(users[0][0])
# # print(users[1])
# # print(users[2])

# for list_ in users:
#     for element in list_:
#         print(element, end=' ')


