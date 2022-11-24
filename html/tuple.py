# tuple - неизменяемый список
# литералы кортежей запятые
# Упорядочный тип данных 
# (), tuple()
# my_tuple = 'Alice', 3, True, False, [1, 2]
# print(type(my_tuple))

# my_tuple = ('Makers',) # Если в кортеже один обьект не забываем в конце ставить запятую
# print(type(my_tuple))


# my_tuple = tuple('Makers')
# print(my_tuple)



# my_typle  = (1, 4, 2, 7, 5) # Поддерживает индексацию 
# print(my_typle[1])
# print(my_typle[-1])
# print(my_typle[::-1])


# print(dir(tuple))

# my_tuple = (1, 4, 4, 7, 4, 2)
# print(my_tuple.count(4))

#index()
# my_tuple = 1, True, 'makers', 9.1
# print(my_tuple.index('makers'))

# len(), max(), min(), sum()
# numbers = 1, 2, 3, 4, 5, 7
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


# my_tuple = 1, True, ['hello', 'world'] # Если в кортеже есть изменяемый тип данных то его можно изменить
# my_tuple[-1][0] = 'bootcamp'
# print(my_tuple)

# empty tuple 
# a = ()
# b = ()
# print(type(a)) # Пустые кортежи сылаются на одну ячейку памяти
# print(type(b))
# print(a is b)
# print(id(a))
# print(id(b))
# a = []
# b = []
# print(a is b)
# print(id(a))
# print(id(b))

# for 
# my_tuple  = ('Alice', 'Sam', 'Cat', 'John')
# for name in my_tuple:
#     print(f'hello {name}')
# my_set = {1, 2, 3, 4, 5}
# for number in my_set:
#     print(number ** 3)

# Цикл While 
# while логическое выражение:
#     body 

# users = {'Alice', 'John', 'Carly', 'Bob'}
# while users :
#     users.pop()
#     print(users)
# print('Program is finished')

# while True:
#     print('THis is loop')

# while True:
#     word = input('Enter the word:')

#     if word.lower() == 'exit':
#         break
#     elif not word:
#         print('Type anything')
#         continue
#     print(word[::-1])

# print('Thks')

# money = 1000
# while money > 0:
#     n = int(input('How much money did you spend: '))
#     money -= n
#     if n > money:
#         print('You do not have enough money')
#         break
#     print(f'You have {money} soms left')

# print('You do not have money')