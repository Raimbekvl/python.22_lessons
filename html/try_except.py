# # try:  - Попробый сделать это если выйдет исключение то переходи к следующему
#     some code 1 
# except:
#     some code 2
# else: # если ексепт не выполнился 
#finaly: # Всегда работает 


# try:
#      num1 = int(input('Chislo'))
# except:
#     print('Вы вели не число !')

# try:
#     num1 = int(input('First num:'))
#     num2 = int(input('Second num:'))
#     result = num1 / num2
# except: # Голое исключение он ловит любую ошибку 
#     print('Вы ввели не число ')
# except Exception as e: # Что бы увидеть ошибку
#     print(e)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вы ввели не число ')
# else:
#     print(result)
# finally:
#     print('Programm finished')



############################################################
# dict_ = dict.fromkeys(('Hello', 'makers', 'bootcamp', 'dictianory'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# print(dict_)
# dict_.update({'except': 'Exception'})
# print(dict_)

# while True:
#     try:
#         key = input('Введите слово:')
#         if key == 'exit':
#             break 
#         dict_[key] += 2
#         print(dict_)
#     except (KeyError, TypeError):
#         print('Данного ключа нет либо конкент. нельзя провести с числами')
#     # except TypeError:
#     #     print('Вы не можете провести конкетенацию с числами ')
#     else:

#         print(dict_[key])
#     finally:
#         print(dict_)

#########################################################

# list_ = [i for i in range(1, 31)]

# try:
#     index = int(input('Ведите индекс:'))
#     list_[index] = 'Makers'
# except IndexError:
#     print('Такого индекса нет в списке')
# except ValueError:
#     print('Please enter the number, not a string')
# else:
#     print('There is no exception')
# finally:
#     print(list_)

########################################################

# try:
#     print(makers)
# # except Exception as e:
# #     print(e)
# except NameError:
#     print('Вы не создавали переменную makers')

##########################################################

# raise

# number = int(input('Введите число от 1 до 70: '))
# if not number in range(1, 71):
#     raise Exception('Вы ввели число, которое не находится в данном промежутке')
# else:
#     print('Okey')





# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [x if x < 0 else x ** 2 for x in list_]
# print(list_)