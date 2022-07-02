# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os
import os.path


def starter():
    """
Create starter with:
1) ONE root folder 'settings'; and
2) FOUR internal folders 'settings', 'mainapp', 'aminapp', 'authapp'
    """
    dir_list = ['settings', 'mainapp', 'aminapp', 'authapp']
    for dir in dir_list:
        dir_path = os.path.join('my_project', dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# Нажмите на старт, чтобы выполнилась функция и создались папки
starter()