# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

import random
file_name = "Data5_5.txt"
usr_count = int(input("Введите количество случайных числел:"))
data_output = ""
for i in range(usr_count):
    data_output = data_output + str(random.randint(1, 99)) + " "

with open(file_name, "w+") as f_obj:
    f_obj.write(data_output)
    f_obj.seek(0)
    content = f_obj.readline().split()
common_sum = 0
for el in content:
    common_sum = common_sum + int(el)
print(f"Сумма числе в файле: {common_sum}")

# Input file "Data5_5.txt":
# 57 65 73 23 53 90 37 75 72 79 93 59

# Output:
# Введите количество случайных числел:12
# Сумма числе в файле: 776
#
# Process finished with exit code 0
