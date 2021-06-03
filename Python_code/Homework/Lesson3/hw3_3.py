# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


# Первый способ, костыльный: исходим из максимальной суммы
def return_max_sum_of_two_args(x, y, z):
    # arg_list = [x, y, z]
    return max(x+y, x+z, y+z)


# Второй способ, костыльный: поиск и сложение двух максимальных аргументов из трех
def return_sum_of_two_max_args_from_three(x, y, z):
    list_arg = [x, y, z]
    list_arg.sort()
    return sum(list_arg[1::])


# Третий способ, универсальный: поиск и сложение двух максимальных аргументов из множества
def return_sum_of_two_max_args(*args):
    tmp_lst = list(args)
    tmp_lst.sort()
    return sum(tmp_lst[-2:])


print(return_max_sum_of_two_args(9, 3, 8))
print(return_sum_of_two_max_args_from_three(5, 1, 9))
print(return_sum_of_two_max_args(4, 5, 6, 7, 8, 2, 0, 3))


# Output
# 17
# 14
# 15
#
# Process finished with exit code 0