# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


# Первый способ
def return_degree(x, y):
    return x**y


# Второй способ
def return_degree_by_cycle(x, y):
    if y == 0:
        return 1
    i = 1
    result = x
    while i < abs(y):
        result *= x
        i += 1
    if y < 0:
        return 1/result
    else:
        return result


usr_x, usr_y = 6, 0
print(f"Эталон: x={usr_x} в степени y={usr_y} равно: {pow(usr_x, usr_y)}")
print(f"Возведение в степень через **: {return_degree(usr_x, usr_y)}")
print(f"Возведение в степень через цикл: {return_degree_by_cycle(usr_x, usr_y)}")


# Output 1: y<0
# Эталон: x=6 в степени y=-5 равно: 0.0001286008230452675
# Возведение в степень через **: 0.0001286008230452675
# Возведение в степень через цикл: 0.0001286008230452675
#
# Process finished with exit code 0


# Output 2: y>0
# Эталон: x=3 в степени y=7 равно: 2187
# Возведение в степень через **: 2187
# Возведение в степень через цикл: 2187
#
# Process finished with exit code 0


# Output 3: y == 0
# Эталон: x=6 в степени y=0 равно: 1
# Возведение в степень через **: 1
# Возведение в степень через цикл: 1
#
# Process finished with exit code 0