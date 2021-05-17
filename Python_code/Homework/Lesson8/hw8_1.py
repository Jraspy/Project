# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = dd_mm_yy

    @classmethod
    def date_to_dict(cls, dd_mm_yy):
        date_lst = dd_mm_yy.split("-")
        return {"День": int(date_lst[0]), "Месяц": int(date_lst[1]), "Год": int(date_lst[2])}

    @staticmethod
    def is_date_correct(dd_mm_yy):
        day = int(dd_mm_yy.split("-")[0])
        month = int(dd_mm_yy.split("-")[1])
        return 1 < day < 31 and 1 < month < 12


usr_date = input("Введите дату в формате день-месяц-год: ")
print(Data.date_to_dict(usr_date))
print(Data.is_date_correct(usr_date))


# Output1:
# Введите дату в формате день-месяц-год: 13-05-2021
# {'День': 13, 'Месяц': 5, 'Год': 2021}
# True

# Output2:
# Введите дату в формате день-месяц-год: 32-13-2111
# {'День': 32, 'Месяц': 13, 'Год': 2111}
# False
#
# Process finished with exit code 0