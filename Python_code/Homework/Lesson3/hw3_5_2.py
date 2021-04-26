# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.


exit_char = chr(35)
usr_sum = 0
is_cycle_complete = False
while not is_cycle_complete:
    print(f"Для выхода введите символ '{exit_char}'")
    usr_str = input("Введите строку чисел через пробел:").split()
    for item in usr_str:
        if item.isdigit():
            usr_sum = usr_sum + int(item)
        elif item == exit_char:
            is_cycle_complete = True
            break
    print(f"Общая сумма: {usr_sum}")


# Output2:
# Для выхода введите символ '#'
# Введите строку чисел через пробел:1 12
# Общая сумма: 13
# Для выхода введите символ '#'
# Введите строку чисел через пробел:1 1 2
# Общая сумма: 17
# Для выхода введите символ '#'
# Введите строку чисел через пробел:10 10 1# 10 # 100 500
# Общая сумма: 47
#
# Process finished with exit code 0