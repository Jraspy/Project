# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_name = "data_file.txt"
is_exit = False
data_lst = []
print("Введите данные для записи в файл (окончание - пустая строка)")
while not is_exit:
    usr_string = input()
    if usr_string != "":
        data_lst.append(usr_string)
    else:
        is_exit = True
with open(file_name, 'w') as f_obj:
    f_obj.writelines(el+"\n" for el in data_lst)
print(f"Введеные даные запианы в файл {file_name}")


# Output:
# Введите данные для записи в файл (окончание - пустая строка)
# Строка один фывфвыфыв
# Строка двадвадва два два
# Строка три три 333
# Четыре 444 44
# пять строка пятьстрока
#
# Введеные даные запианы в файл data_file.txt
#
# Process finished with exit code 0


# Content of data_file.txt:
# Строка один фывфвыфыв
# Строка двадвадва два два
# Строка три три 333
# Четыре 444 44
# пять строка пятьстрока
#