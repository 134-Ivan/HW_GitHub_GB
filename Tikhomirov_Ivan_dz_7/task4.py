# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import random
import os.path
import os


def folder_with_rand_files_creator(folder_name):
    dir_path = os.path.join(folder_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        for file in range(int(random.random()*100)):
            with open(f"{dir_path}/{file}_to_create.txt", "w") as f:
                content = []
                for i in range(int(random.random() * 1_000)):
                    content.append(i)
                    f.write(f'{content}')


folder_with_rand_files_creator('task_4_folder')

files_list = []
# for folder in os.listdir('task_4_folder'):
#     files_list.append(folder)
#
# print(files_list)
#
# files_size =[]
# for folder in os.listdir('task_4_folder'):
#     files_size.append(os.path.getsize(folder))
#
# print(files_size)
#
