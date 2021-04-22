# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_value = input("Enter value: ")
value_int = int(user_value)

new_value = value_int
max_value = 0
while new_value != 0:
    dif = new_value % 10
    new_value = new_value // 10
    if max_value <= dif:
        max_value = dif
print(f"Maximum is: {max_value}")
