# file1 = open('/home/hello/Desktop/makers/html/files/makers.txt', 'r')
# print(file1.read())

##########################

# r - read()   #только для чтения
# r+ - read + write  # Для чтения и для записи 
# w - write # для записи  и если есть запись то он удаляет и пишет свою инфу
# w+ - read + write 
# a - append  # Добовляем в конец  и не удаляет инфу в файле
# a+ - append + read 
# x - write  # он открыт для записи если файла не существует и он создает новый 
# b - binary   #открытие в двоичном режиме
# t - text 
# rt -> r 
# rb -> 


# file1 = open('makers.txt', 'r')
# data = file1.read()
# print(data)
# print(type(data))

# file1 = open('makers.txt', 'r')
# data = file1.read(3)   # Возвратит первые 3 символа
# print(data)


# file1 = open('makers.txt', 'r')
# print(file1.read(10)) # считал первые 10 символов до 10
# print(file1.read(10)) # а тут он продолжыл считывание с 10
# file1.seek(0) # Прерывает и возвращает на начало 
# print(file1.read(5)) 
#seek()Прерывает и возвращает на начало



# file1 = open('makers.txt', 'r')
# # file1.readline() # Построчно нам возвращает данные из текста 
# for line in file1:
#     print(line)


# file1 = open('makers.txt', 'r')
# list_ = file1.readlines() #  Считывает файл в список 
# print(list_)

# for line in list_:
#     print(line)

# file1 = open('makers.txt', 'r')
# list_ = file1.readlines()
# list_ = [x.replace('\n', '') for x  in list_]
# print(list_)


###########################################################
# file2 = open('bootcamp.txt', 'a')
# print(file2.write('Makers' + '\n'))


# file2 = open('bootcamp.txt', 'w')
# # file2.write("It's such a beautiful day today" + '\n')
# # file2.write('Today is my birthday')


# list_mottos = ['Just do it ', 'Just watch', 'Got Milk ?']
# list_mottos = [motto + '\n' for motto in list_mottos]
# file2.writelines(list_mottos)
# dict_ = {
#     'name': 'Makers',
#     'hello': 'world'
# }
# file2.writelines(dict_)  # Получим только ключи в файл 



############################################################
# file3 = open('makers2.txt', 'x')  #  Отличие x от w  в том что x нужен для создание файла а если существует такой файл то выдаст ошибку его редко используют 
# print(file3.write('Bootcamp' + '\n'))


##############################################################

# file3 = open('files.txt', 'a')

# list_mottos = ['Just do it ', 'Just watch', 'Got Milk ?']
# list_mottos = [motto + '\n' for motto in list_mottos]

# file3.write('Mottors of big companies' + '\n')
# for motto in list_mottos:
#     file3.write(motto)

# file3.close() # ВСЕГДА НУЖНО ЗАКРЫВААТЬ ФАЙЛ ДЛЯ БЕЗОПАСНОСТИ  
# print(file3.closed())

# with open('files.txt') as my_file: # При таком виде работы не обязательно закрывать в конце файл в этом и плюс
#     print(my_file.read())   



# with open('files.txt', 'r+') as my_file:  # Если записать w+ то файл перезапишится  в этом и есть разница
#     print(my_file.read())
#     my_file.write('Additional stringy')
# print(my_file.closed) # Всегда вне конструкции with закрывается файл автоматическ и вне кострукции нельзя будет изменить

####################################################################

# math, random, datetime 

# import square 
# print(square.circle(5))


# from square import circle, triangle, rectangle 

# circle_area = circle(8)
# triangle_area = triangle(9, 6)
# rectangle_area = rectangle(4, 6)
# print(circle_area, triangle_area, rectangle_area)

###################################################################


# Task 1 
# with open('numbers.txt', 'w') as file1:
#     for number in range(1, 21):
#         file1.write(str(number) + '\n')


# with open('squares.txt', 'w') as file2:
#     with open('numbers.txt') as file1:
#         data = file1.read().split('\n')
#         data.pop()
#         new_data = list(map(int, data))
#         print(new_data)
#         for number in new_data:
#             file2.write(str(number ** 2) + '\n')

# with open('numbers.txt') as file1:
#     list_ = file1.readlines(8)
#     list_ = [x.replace('\n', '') for x in list_]
#     print(list_)


# Task 2 
# with open('username.txt', 'w') as my_file:
#     while True:
#         username = input('Enter username:')
#         if username.lower() == 'end':
#             break 
#         my_file.write(f'{username} - {len(username)}]\n')


# with open('squares.txt', 'w') as file1:
#     for num in range(10):
#         file1.read(str(num))
# with open('numbers.txt', 'w') as file1:
#     for number in range(1, 21):
#         file1.write(str(number) + '\n')
#######################################################
# with open('num.txt', 'w+') as file:
#     for num in range(10):
#         file.write(str(num) + '*')
    
# with open('num.txt') as file1:
#     print(file1.read())
    

# with open('task4.txt') as file:
#     line_count = sum(1 for line in file)
#     print(line_count)

with open('task5.txt', 'r') as file:
    m = []
    full_f = file.read()
    for i in full_f.split():
        m.append(int(i))

with open('task6.txt', 'w') as f:
    print('max_num = ', max(m), file=f)
    print('min_num = ', min(m), file=f)