# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

file_name = "Data5_3.txt"
i = 0
common_salary = 0
with open(file_name, "r") as f_obj:
    for line in f_obj:
        i += 1
        data = line.split()
        salary = int(data[1])
        if salary < 20000:
            print(f"Оклад менее 20к: {data[0]} = {salary}")
        common_salary = common_salary + salary

print(f"Средняя величина дохода сотрудника: {common_salary / i}")

# Content of data_file.txt:
# Ivanov 10000
# Petrov 22000
# Sidorov 15000
# Pypkin 25000

# Output:
# Оклад менее 20к: Ivanov = 10000
# Оклад менее 20к: Sidorov = 15000
# Средняя величина дохода сотрудника: 18000.0
#
# Process finished with exit code 0