# empty_set = set()
# Литереалы сетов фигурные скобки как у словаря  
# print(type(empty_set))
# empty_dict = {}
# print(type(empty_dict))

# a = {'makers', 4, 9, True, False}
# print(type(a))
# b = set('makers') # Множество не упорядочный тип данных
# print(b)
# print(a)
# c = set(range(1,20,2))
# print(c)

# my_set = {'hello', 1, False} # Множество может хранить только не изменяемые тип данных
# print(my_set)
# my_set1 = {[]} - Выдаст ошибку потому что списки изменяемые тип данных


# set1 = {1, 5, 3, 9, 8}
# set2 = {9, 1, 5, 3, 8}
# set3 = {1, 5, 1, 3, 3, 8, 8, 8, 9, 9}
# print(set3) # Сет хранит только уникальные значение дубликаты он удаляет
# print(set1 == set2) #- Подтверждает что порядок не важен
# print(set3 == set2)


# my_set = {True, 1, 1.0} # Значение всех элементов по значению равны и удаляет дубликаты
# print(my_set)


# set3 = {1, 5, 1, 3, 3, 8, 8, 8, 9, 9}
# print(set3)
# print(len(set3))


# quests = {'Tom', 'Sam', 'John', 'Tom'}
# print(len(quests))

#Методы множеств 

# add() - Добавляет элемент во множество 

# quests = {'Tom', 'Sam', 'John', 'Emily'}
# print(quests)
# quests.add('Raychel')
# quests.add('Tom')
# print(quests)

# #update() Расширяет за счет другого
# numbers1 = {1, 2, 3, 4, 5}
# numbers2 = {6, 7, 8, 9, 10}

# numbers1.update(numbers2)
# print(numbers1)

#remove() - удаляет эелемент
# quests = {'Cat', 'Alice', 'Carly', 'Ben'}
# quests.remove('Alice')
# print(quests)

# discard - удаляет элемент, Разница в том то что если элемента нету то нам 
# вазвращается просто множество а
#в remove выдает ошибку если нет обьекта
# quests = {'Cat', 'Alice', 'Carly', 'Ben'}
# quests.discard('Alice')
# print(quests)

# pop() - удаляет элемент, каждый раз удаляет любой элемент рандомно 
# quests = {'Cat', 'Alice', 'Carly', 'Ben'}
# quests.pop()
# print(quests)

# clear()
# quests = {'Cat', 'Alice', 'Carly', 'Ben'}
# quests.clear()
# print(quests)

# copy() - копирует 
# quests = {'Cat', 'Alice', 'Carly', 'Ben'}
# quests2 = quests.copy()
# quests.add('Raychel')
# print(quests)
# print(quests2)



# itersection() находит пересечение двух множеств 
# music_students = {'Sam', 'Alice', 'Kate',
#                   'Ben', 'John'}
# art_students = {'Raychel', 'Sam', 'John',
#                 'Cathrine'}
# it_students = {'Sam', 'Tom'}
# print(music_students.intersection(art_students))
# print(music_students & art_students & it_students) # может и такое 

# union()   обьединяет множество 
# music_students = {'Sam', 'Alice', 'Kate',
#                   'Ben', 'John'}
# art_students = {'Raychel', 'Sam', 'John',
#                 'Cathrine'}
# it_students = {'Sam', 'Tom', 'Aibek'}
# print(art_students.union(music_students)) # Получаем обьединененую множество без дубликатов 
# print(art_students | music_students | it_students) # И так можно 





#differnece() находит разность 

# music_students = {'Sam', 'Alice', 'Kate',
#                   'Ben', 'John'}
# art_students = {'Raychel', 'Sam', 'John',
#                 'Cathrine'}
# print(music_students.difference(art_students)) # Эти элементы не входят во вторую группу 
# print(music_students - art_students) # И так можно с оператором -




# symetric_difference() - он вазвращает нам уникальные элементы для обоих множеств 

# music_students = {'Sam', 'Alice', 'Kate',
#                   'Ben', 'John'}
# art_students = {'Raychel', 'Sam', 'John',
#                 'Cathrine'}
# print(music_students.symmetric_difference(art_students)) # Находит для обоих уникальные не пересекающие элементы



#isdisjoin() возвращает True or False есть ли какие либо пересечения  
# num1 = {1, 2, 3, 4}
# num2 = {7, 5, 6}
# print(num1.isdisjoint(num2)) # Если нету True а если есть то False


#issuperset() - Надмножество , issubset()- подмножесто , возвращает True or Flase 

# a = {1, 2, 3, 4, 5}
# b = {3, 5}
# print(a.issuperset(b))


#intersection_update() - Изменяет и доб пересек элементы

# num1 = {1, 2, 3, 4}
# num2 = {2, 5, 1}
# num1.intersection_update(num2)
# print(num1) # Теперь в  num1 хранится пересекающие элементы

#difference_update() 
# num1 = {1, 2, 3, 4, 5, 6}
# num2 = {5, 2, 7, 8}
# num2.difference_update(num1)
# print(num2) # Хранятся только уникальные для этого множество ключи 


# symmetric_difference_update()
# num1 = {1, 2, 3, 4, 5}
# num2 = {6, 9, 0, 2, 4}
# num1.symmetric_difference_update(num2) # Хранит для обоих уникальные значеия 
# print(num1)

# Замороженное множество , отличие от обычного в том что его нельзя изменить 
# my_frozenset = frozenset()
# print(type(my_frozenset))
# my_frozenset = frozenset('makers')
# my_frozenset.add('b')
# print(my_frozenset) # Нельзя изменить 
