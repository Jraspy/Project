# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

numeral_rus = {0: "Ноль",
               1: "Один",
               2: "Два",
               3: "Три",
               4: "Четыре",
               5: "Пять",
               6: "Шесть",
               7: "Семь",
               8: "Восемь",
               9: "Девять",
               10: "Десять",
               11: "Одинадцать",
               12: "Двенадцать"}
file_name = "Data5_4.txt"


def translate_2_rus(common_line):
    data_set = common_line.split()
    last_index = int(data_set[len(data_set)-1])
    data_set[0] = numeral_rus.get(last_index)
    return " ".join(data_set)


translated_lines = []
with open(file_name, "r") as f_obj:
    for line in f_obj:
        translated_lines.append(translate_2_rus(line))
with open("translated_" + file_name, "w") as f_obj:
    f_obj.writelines(el + "\n" for el in translated_lines)


# Input file "Data5_4.txt":
# One - 1
# Two - 2
# Three - 3
# Four - 4
# Five - 5
# Six - 6
# Seven - 7

# Output:
#
# Process finished with exit code 0

# Output file "translated_Data5_4.txt":
# Один - 1
# Два - 2
# Три - 3
# Четыре - 4
# Пять - 5
# Шесть - 6
# Семь - 7
