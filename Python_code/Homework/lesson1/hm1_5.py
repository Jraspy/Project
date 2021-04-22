# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

proceeds = int(input("Enter year proceeds, $: "))
costs = int(input("Enter year costs, $: "))
profit = proceeds - costs
if profit > 0:
    print(f"Likely year! Your profit is ${profit}!")
    profit_index = profit / proceeds
    print(f"Profitability index is: {profit_index}")
    employee_count = int(input("How many employees, persons: "))
    profit_per_employee = profit / employee_count
    print(f"Personal profit is, $/person: {profit_per_employee}")
elif profit < 0:
    print(f"Losses year =( No profit - no income taxes!")
    print(f"Financial damage is: $ {profit}")
else:
    print("Zero")
