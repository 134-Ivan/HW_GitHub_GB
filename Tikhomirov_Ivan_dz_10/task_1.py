# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

first_m = [
    [31, 22],
    [37, 43],
    [51, 86]
]

second_m = [
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8]
]

third_m = [
    [31, 22],
    [37, 43],
    [51, 86]
]

fourth_m = [
    [3, 5, 8, 3],
    [8, 3, 7, 1]
]



class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        if len(self.matrix_list) != len(other.matrix_list) or len(self.matrix_list[0]) != len(other.matrix_list[0]):
            print('no match of matrix size')
        else:
            new_matrix = []
            for i in range(len(self.matrix_list)):
                row = []
                for j in range(len(self.matrix_list[0])):
                    row.append(self.matrix_list[i][j] + other.matrix_list[i][j])
                new_matrix.append(row)
            return new_matrix

    def __str__(self):
        if len(self.matrix_list) == 2:
            new_matrix = ''
            for items_list in self.matrix_list:
                for item in items_list:
                    new_matrix += str(item)
                    new_matrix += ' '
                new_matrix += '\n'
            return f'{new_matrix}'
        elif len(self.matrix_list) == 3:
            new_matrix = ''
            for items_list in self.matrix_list:
                for item in items_list:
                    new_matrix += str(item)
                    new_matrix += ' '
                new_matrix += '\n'
            return f'{new_matrix}'



mx_1 = Matrix(first_m)
mx_2 = Matrix(second_m)
mx_3 = Matrix(third_m)
mx_4 = Matrix(fourth_m)


print(mx_1.matrix_list)
print(mx_2.matrix_list)
print(mx_3.matrix_list)
print(mx_4.matrix_list)

print(mx_1)
print(mx_2)
print(mx_3)
print(mx_4)


print(mx_1 + mx_3)
print(mx_1 + mx_2)