# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(input_str):
    return input_str.title()


usr_str = input("Введите слово: ").split()
title_list = []
for item in usr_str:
    title_list.append(int_func(item))
print(*title_list)

# Output:
# Введите слово: text1 text2 text3 text4
# Text1 Text2 Text3 Text4
#
# Process finished with exit code 0
