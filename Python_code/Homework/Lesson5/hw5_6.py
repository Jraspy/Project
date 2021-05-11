# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
# все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import codecs


def get_lesson_name(income_line):
    return income_line.split(":")[0]


def get_lesson_hours(income_line):
    hours_lst = []
    value = ""
    for el in income_line:
        if el.isdigit():
            value = value + el
        elif value != "":
            hours_lst.append(int(value))
            value = ""
    return sum(hours_lst)


common_count_lessons = {}
file_name = "Data5_6.txt"
with codecs.open(file_name, encoding='utf-8') as f_obj:
    for line in f_obj:
        common_count_lessons.update({get_lesson_name(line): get_lesson_hours(line)})
print(common_count_lessons)


# Input file:
# Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Программирование:   50(л)   60(контрольные)   — и чтото там еще

# Output:
# {'Информатика': 170, 'Физика': 40, 'Физкультура': 30, 'Программирование': 110}
#
# Process finished with exit code 0