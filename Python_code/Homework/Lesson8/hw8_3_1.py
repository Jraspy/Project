# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class CustomException(Exception):
    def __init__(self, txt):
        self.txt = txt


exit_str = "stop"
usr_str = ""
result_lst = []
while usr_str != exit_str:
    usr_str = input(f"Введите элемент списка из чисел (для завершения введите {exit_str}): ")
    if usr_str != exit_str:
        try:
            if not usr_str.isdigit():
                raise CustomException(f"Ошибка! Введеные данные '{usr_str}' отличны от чисел!")
        except CustomException as err:
            print(err)
        else:
            result_lst.append(int(usr_str))
print(f"Результат: {result_lst}")

# Output:
# Введите элемент списка из чисел (для завершения введите stop): 33
# Введите элемент списка из чисел (для завершения введите stop): 55
# Введите элемент списка из чисел (для завершения введите stop): ggt
# Ошибка! Введеные данные 'ggt' отличны от чисел!
# Введите элемент списка из чисел (для завершения введите stop): gt44
# Ошибка! Введеные данные 'gt44' отличны от чисел!
# Введите элемент списка из чисел (для завершения введите stop): stop
# Результат: [33, 55]
#
# Process finished with exit code 0