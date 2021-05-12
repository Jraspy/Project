# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

import random


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix_list = list_of_lists

    def __str__(self):
        temp_str = ""
        for el_lists in self.matrix_list:
            for el in el_lists:
                temp_str = temp_str + str(el) + ' '
            temp_str = temp_str[:-1] + '\n'
        return temp_str

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list):
            result = []
            for el_self_list, el_other_list in zip(self.matrix_list, other.matrix_list):
                temp_result = []
                for el_self, el_other in zip(el_self_list, el_other_list):
                    temp_result.append(el_self + el_other)
                result.append(temp_result)
            return result
        else:
            print("Длина матриц не совпадает!")


def list_of_lists_generator(size_x: int, size_y: int, random_range_start=-10, random_range_stop=10):
    result = []
    for x in range(size_x):
        temp_lst = []
        for y in range(size_y):
            temp_lst.append(random.randint(random_range_start, random_range_stop))
        result.append(temp_lst)
    return result


x, y = 3, 3
matrix = Matrix(list_of_lists_generator(x, y))
print(matrix)

matrix2 = Matrix(list_of_lists_generator(x, y))
print(matrix2)

matrix3 = Matrix(matrix + matrix2)
print(matrix3)


# Output:
# 9 3 -8
# 10 4 -8
# -4 1 2
#
# -7 -8 -2
# 9 1 5
# -10 7 10
#
# 2 -5 -10
# 19 5 -3
# -14 8 12
#
#
# Process finished with exit code 0