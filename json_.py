# java scrip notation object

# dump(), dumps()


# import json

# info = {
#     "name": "Alice",
#     "age": 79,
#     "book": "Chamber of Secrets"
# }


# with open('info.json', 'w') as file: # Сериализация 
#     json.dump(info, file)


# json_object  = json.dumps(info)
# print(json_object)
# print(type(json_object))

############################################################


# load(), loads()

# import json

# with open('info.json') as file: # Дессериализация
#     python_object = json.load(file)
#     print(python_object)
#     print(type(python_object)) # Возвращает нам в питонский обьект в виде словаря
    
# python_object['name'] = 'John'
# print(python_object)

# with open('info.json', 'w') as file:
#     json.dump(python_object, file)

###########################################################
# loads()

# import json

# json_str = '{"name": "Alice", "age": 79, "book": "Chamber of secret"}'
# python_object = json.loads(json_str)
# print(json_str)
# print(python_object)
# python_object.update({'color': 'yellow'})
# print(python_object)


##########################################################


# import json

# with open('task1.json') as file1:
#     python_object = json.load(file1)
#     print(python_object)

# with open('task1.py', 'w') as file2:
#     file2.write(str(python_object))

############################################################

# import json 

# json_obj = "null"

# python_obj = json.loads(json_obj)
# print(python_obj)

###########################################################


import json

users = [
    {
        'name': 'John',
        'last_name': 'Snow',
        'age': 26,
        'has_car': True,
    },
    {
        'name': 'Sam',
        'last_name': 'Bolt',
        'age': 4,
        'has_car': False,
    }
]

json_object = json.dumps(users)

with open('task1.json', 'w') as file:
    json.dump(json_object, file)