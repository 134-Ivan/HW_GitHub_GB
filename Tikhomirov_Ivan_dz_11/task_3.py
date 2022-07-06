# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.



class NumListChecker(Exception):
    def __init__(self, text):
        self.text = text

user_list = []

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

while True:
    inp_data = input('Введите данные: ')
    try:
        if inp_data.isdigit():
            user_list.append(inp_data)
            print(user_list)
        elif is_number(inp_data):
            user_list.append(inp_data)
            print(user_list)
        else:
            raise NumListChecker('Ошибка: Вы ввели не число')
    except NumListChecker as err:
        print(err)






