#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_value = input("Enter value [1...9]: ")
value_int = int(user_value)
sum_value = value_int + value_int * 11 + value_int * 111
print(f"{sum_value} = {value_int} + {value_int * 11} + {value_int * 111}")
