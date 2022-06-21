# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.



class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self, weight_one_meter, layer_width):
        print(self._length * self._width * (weight_one_meter/100) * layer_width/10)


highway_to_hell = Road(20, 5000)

highway_to_hell.asphalt_weight(25, 5)
