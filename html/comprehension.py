# for 
# list_ = []
# for i in range(1, 21):
#     list_.append(i * 2)

# print(list_)

#list comprehension
 
# list_ = [num * 2 for num in range(1, 21)]
# print(list_)

# list_users = ['Alice', 'Sam', 'Sandy', 'Ben', 'John']
# invitations = ['You are invited ' + name for name in list_users]
# print(invitations)


# list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 or num % 3 == 0]
# print(list2)

# strings = ['1998', '2001r', '2008year', '2020']
# list_ = [year for year in strings if year.isdigit()]
# print(list_)

# list_ = ['Raychel', 'John', 'Alice', 'Sam']
# list_ = [len(name) for name in list_]
# print(list_)

# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [x if x < 0 else x ** 2 for x in list_]
# print(list_)


# list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list_ = [x if x < 0 else x ** 2 for x in list_ if x  % 2 == 0]
# print(list_)

# names = ['raychel', 'john', 'peter', 'jessica', 'bill', 'steven', 'steven123', 'sandy45', 'james']
# filtered_names = [
#     x + 'MAKERS' 
#     if len(x) >= 5 
#     else x + 'makers' 
#     for x in names 
#     if x.isalpha()
#     ]
# print(filtered_names)

# filtered_names = []
# for x in names:
#     if x.isalpha():
#         if len(x) >= 5:
#             result = x + 'MAKERS'
#             filtered_names.append(result)
#         else:
#             result = x + 'makers'
#             filtered_names.append(result)

# print(filtered_names)

# john = {'name': 'John', 'age': 22}
# raychel = {'name': 'Raychel', 'age': 23}
# peter = {'name': 'Peter', 'age': 17}

# users = [john, raychel, peter]
# ages = [user.get('age', None) for user in users]
# bigger = 0
# smaller = 0
# count = 0
# for age in ages:
#     if age >= 18:
#         bigger += 1
#     else:
#         smaller += 1
#     count += 1
# bigger = bigger * (100/count)
# smaller = smaller * (100/count)

# print(ages)
# print(bigger)
# print(smaller)
# print(count)


# matrix = [
#     [0, 2, 5, 6],
#     [7, 3, 0, 7],
#     [5, 7, 1, 6]

# ]

# uncompress = [n for row in matrix for n in row]

# uncompress = []
# for row in matrix:
#     for n in row:
#         uncompress.append(n)

# print(uncompress)

# from datetime import datetime

# start = datetime.now()
# print(start)

# list_ = [i for i in range(100000)]
# # list_ = []
# # for i in range(100000):
# #     list_.append(i)

# print(datetime.now() - start)


# dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': -4, 'e': -7}
# # dict_123 = {key.upper(): value + 2 for key, value in dict_abc.items()}
# # print(dict_123)
# new_dict = {key.upper(): value ** 3 for key, value in dict_abc.items() if value > 0}
# print(new_dict)

# a = {'fruits':{'apple': 100, 'orange': 60}, 'vegetables': {'cocumbers': 28, 'tomato': 63}}
# b = {key: {inner_k: inner_v + 3 for inner_k, inner_v in value.items()} for key, value in a.items()}
# print(b)

# list_ = [num for num in range(1, 50) if num % 2 != 0]
# print(list_)



# my_dict = {num**2 : num for num in range(11)} 
# print(my_dict) 



# n = int(input('1-10:'))
# dict_ = {num:num**2 for num in range(1, 501) if num % n == 0}
# print(dict_)

# text = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# ls = [x for x in text if x.isdigit()]
# print (ls)