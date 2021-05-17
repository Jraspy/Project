# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class CustomException(Exception):
    def __init__(self, txt):
        self.txt = txt


usr_value1 = input("Введите делимое: ")
usr_value2 = input("Введите делитель: ")

try:
    usr_int1 = int(usr_value1)
    usr_int2 = int(usr_value2)
    if usr_int2 == 0:
        raise CustomException("Ошибка: делитель не можеть быть 0!")
except ValueError:
    print("Ошибка: ")
except CustomException as err:
    print(err)
else:
    print(f"Результат деления: {usr_int1 / usr_int2}")

# Output1:
# Введите делимое: ww
# Введите делитель: 1
# Ошибка: вы ввели не число
#
# Process finished with exit code 0

# Output2:
# Введите делимое: 14
# Введите делитель: 0
# Ошибка: делитель не можеть быть 0!
#
# Process finished with exit code 0

# Output3:
# Введите делимое: 55
# Введите делитель: 11
# Результат деления: 5.0
#
# Process finished with exit code 0