# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def extractor(cls, data):
        day = int(data[1:2])
        month = int(data[3:5])
        year = int(data[6:])
        print(f"число: {day}, тип {type(day)},\n"
              f"месяц: {month}, тип {type(month)}\n"
              f"год: {year}, тип {type(year)}")

    @staticmethod
    def date_validation(data):
        day = int(data[0:2])
        month = int(data[3:5])
        whole_year = {1: 31, 2: 28, 3: 31,
                      4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30,
                      10: 31, 11: 30, 12: 31,
                      }

        if month in whole_year.keys():
            if day <= whole_year[month]:
                print('формат даты верный')
            elif day > whole_year[month]:
                print('неверный формат даты')
        else:
            print('месяц должден быть меньше либо равен 12')

Data.extractor('01-12-2021')
Data.date_validation('01-12-2021')
Data.date_validation('31-02-2021')
Data.date_validation('01-13-2021')

