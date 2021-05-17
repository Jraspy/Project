# 7. Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
profit_data = {}
losses_data = {}
average_profit = {}
file_name = "Data5_7.txt"
file_output = "Data5_7_output.json"
name_index = 0
# ownership_index = 1
income_index = 2
costs_index = 3
count_profits_firms = 0
common_income = 0

with open(file_name) as f_obj:
    for line in f_obj:
        lst = line.split()
        name = lst[name_index]
        income = int(lst[income_index])
        costs = int(lst[costs_index])
        profit = income - costs
        profit_data.update({name: profit})
        if profit >= 0:
            common_income = common_income + profit
            count_profits_firms += 1
        else:
            losses_data.update({name: profit})
average_profit.update({"average_profit": common_income / count_profits_firms})
result_lst = [profit_data, average_profit]
with open(file_output, "w") as f_obj:
    json.dump(result_lst, f_obj)

# Input file:
# firm_1 ООО 10000 5000
# firm_2 ООО 1000 50000
# firm_3 ООО 70000 70000
# firm_4 ООО 40000 30000
# firm_5 ООО 0 36000
# firm_6 ООО 55000 0

# Output file:
# [{"firm_1": 5000, "firm_2": -49000, "firm_3": 0, "firm_4": 10000, "firm_5": -36000, "firm_6": 55000}, {"average_profit": 17500.0}]
