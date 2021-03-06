# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return (f'Сотрудника зовут: {self.name} {self.surname}')
    def get_total_income(self):
        return self.income['wage'] + (self.income['wage'] * self.income['bonus'] / 100)


# ПРИМЕРЫ

ivan = Worker('Ivan', 'Tikhomirov', 'Senior Charterer', 100, 10)
sanja = Worker('Alexander', 'Pikul', 'Charterer', 90, 5)

print(Position.get_full_name(ivan))
print(Position.get_total_income(ivan))

print(Position.get_full_name(sanja))
print(Position.get_total_income(sanja))

