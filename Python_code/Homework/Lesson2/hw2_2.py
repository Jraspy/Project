# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_string = input(f"input string: ")
lst = list(user_string)
print(lst)
count = 0
for item in lst:
    if (count % 2) != 0:
        lst[count-1], lst[count] = lst[count], lst[count-1]
    count += 1
print(f"Result: {lst}")
