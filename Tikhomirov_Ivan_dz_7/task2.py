# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта.

import os.path
import yaml
from yaml.loader import SafeLoader

# НАЖМИТЕ НА ЗАПУСК ПРОГРАММЫ, ЧТОБЫ СФОРМИРОВАТЬ СТРУКТУРУ ПАПОК ИЗ ФАЙЛА CONFIG.YAML

def starter_execution():
    with open('config.yaml', encoding='utf-8') as f:
        starter = yaml.load(f, Loader=SafeLoader)
        for root_folder, layer_one_folders in starter.items():
            for folders_dict in layer_one_folders:
                for folder_name, content in folders_dict.items():
                    dir_path = os.path.join(root_folder, folder_name)
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                        for file in content[:3]:
                            if file.endswith('.py'):
                                with open(f'{root_folder}/{folder_name}/{file}', 'w') as f:
                                    f.write(file)
                        for file in content[3:4]:
                                    dir_path_2 = os.path.join(f'{root_folder}/{folder_name}/', file)
                                    if not os.path.exists(dir_path_2):
                                        os.makedirs(dir_path_2)
                        for file in content[4:5]:
                                    dir_path_3 = os.path.join(dir_path_2, file)
                                    if not os.path.exists(dir_path_3):
                                        os.makedirs(dir_path_3)
                        for file in content[5:]:
                                    with open(f'{dir_path_3}/{file}', 'w') as f:
                                        f.write(file)

starter_execution()

