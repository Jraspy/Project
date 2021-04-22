# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rate_list = [7, 5, 3, 3, 2]
print(f"Default rate list: {rate_list}")
usr_rate = int(input("Enter new rate: "))
position = 0
if usr_rate in rate_list:
    count_entry = rate_list.count(usr_rate)
    position_entry = rate_list.index(usr_rate)
    position = position_entry + count_entry
else:
    for item in rate_list:
        if usr_rate > item:
            position = rate_list.index(item)
            break
        elif usr_rate < item:
            position = rate_list.index(item) + 1
rate_list.insert(position, usr_rate)
print(rate_list)
