# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
scrip_name, usr_hours, usr_rate, usr_bonus = argv


def wage_calc(hours, rate, bonus):
    return float(hours)*float(rate)+float(bonus)


print(f"Выработка в часах: {usr_hours}")
print(f"Ставка в час: {usr_rate}")
print(f"Премия: {usr_bonus}")
print(f"Расчетная ззарплата: {wage_calc(usr_hours, usr_rate, usr_bonus)}")


# Output
# ...Homework>Python Lesson4\hw4_1.py 42 5.5 300
# Выработка в часах: 42
# Ставка в час: 5.5
# Премия: 300
# Расчетная ззарплата: 531.0
