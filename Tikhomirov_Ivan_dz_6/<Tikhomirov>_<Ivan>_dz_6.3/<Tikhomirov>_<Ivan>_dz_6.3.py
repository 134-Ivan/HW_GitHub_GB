# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import itertools

def get_user(file_with_users):
    list_of_users = []
    with open(file_with_users, 'r', encoding='utf-8') as f:
        for line in f:
            list_of_users.append(line.strip())
    return(list_of_users)

def get_hobbies(file_with_hobbies):
    list_of_hobbies = []
    with open(file_with_hobbies, 'r', encoding='utf-8') as f:
        for line in f:
            list_of_hobbies.append(line.strip())
    return(list_of_hobbies)

users = get_user('users.csv')
hobbies = get_hobbies('hobby.csv')

dict_users = {}

try:
    if len(users) == len(hobbies):
        for i in range(0,len(users)):
            dict_users[users[i]] = hobbies[i]
        print(dict_users)
finally:
    if len(users) < len(hobbies):
        print('smth went wrong')


# try:
#     if len(users) >= len(hobbies):
#         combination = dict(itertools.zip_longest(users, hobbies))
#         print(combination)
# except Exception:
#
#         print('la la la')
#
#
