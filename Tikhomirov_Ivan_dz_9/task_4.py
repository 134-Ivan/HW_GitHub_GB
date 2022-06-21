# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print('машина поехала')

    def stop(self):
        return print('машина остановилась')

    def turn(self):
        if 'left':
            print('turn left')
        elif 'right':
            print('turn right')

    def show_speed(self):
        return print(self.speed())


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('please drop the speed')


nissan = TownCar(70, 'red', 'juke', is_police = False)

print(nissan.speed)
nissan.show_speed()
nissan.go()
nissan.stop()
print(nissan.is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('please drop the speed')

bobcat = WorkCar(50, 'yellow', 'JCB', is_police = False)

print(bobcat.speed)
bobcat.show_speed()
bobcat.go()
bobcat.stop()
print(bobcat.is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

ford = PoliceCar(50, 'black', 'pursuit', is_police = True)

print(ford.speed)
ford.go()
ford.stop()
print(ford.is_police)



