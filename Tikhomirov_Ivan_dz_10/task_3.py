# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и округление до целого числа деления клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.

# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.

# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.




class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = int(number_of_cells)

    def __add__(self, other):
        return self.number_of_cells + other.number_of_cells

    def __sub__(self, other):
        return self.number_of_cells - other.number_of_cells

    def __mul__(self, other):
        return self.number_of_cells * other.number_of_cells

    def __floordiv__(self, other):
        return self.number_of_cells // other.number_of_cells

    def __truediv__(self, other):
        return self.number_of_cells / other.number_of_cells

    def make_order(self, row_length):
        self.row_length = row_length
        return f"{'*'* row_length}\\n{'*'* row_length}\\n{'*'*(self.number_of_cells - (2 * self.row_length))}"


cell_1 = Cell(10)
cell_2 = Cell(7)

print(cell_1.make_order(4))
print(cell_2.make_order(3))

# СЛОЖЕНИЕ
print(f'результат сложение: {cell_1 + cell_2}')

# ВЫЧИТАНИЕ
print(f'результат вычитания: {cell_1 - cell_2}')

# УМНОЖЕНИЕ
print(f'результат умножения: {cell_1 * cell_2}')

# ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ
print(f'результат целочисленного деления: {cell_1 // cell_2}')

# ДЕЛЕНИЕ
print(f'результат деления: {cell_1 / cell_2}')

