# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите число: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise Zero('used zero value')
except ValueError:
    print("Вы ввели не число")
except Zero as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {100/inp_data}")


