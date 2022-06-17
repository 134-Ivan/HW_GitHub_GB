# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates.

import shutil
import os
import os.path
from task2 import starter_execution


# НАЖМИТЕ НА ЗАПУСК ПРОГРАММЫ, ЧТОБЫ СФОРМИРОВАТЬ СТРУКТУРУ ПАПОК ИЗ ФАЙЛА CONFIG.YAML

starter_execution()

# СЛЕДУЮЩИЙ КОД ПЕРЕМЕЩАЕТ ШАБЛОНВ В ОДНУ ПАПКУ templates

def templates_collector(root_folder):
    dir_path = os.path.join(root_folder, 'templates')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        shutil.move('my_project/authapp/templates/authapp', 'my_project/templates')
        shutil.move('my_project/mainapp/templates/mainapp', 'my_project/templates')


templates_collector('my_project')