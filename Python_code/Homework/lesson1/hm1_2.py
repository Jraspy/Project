# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_value_sec = input("Enter time in sec, please: ")
value_int = int(user_value_sec)
hours = value_int // 3600
minutes = value_int // 60 % 60
sec = value_int % 60
print(f"HH:MM:SS --> {hours:02}:{minutes:02}:{sec:02}")
