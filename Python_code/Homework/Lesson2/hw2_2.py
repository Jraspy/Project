user_string = input(f"input string: ")
lst = list(user_string)
print(lst)
count = 0
for item in lst:
    if (count % 2) != 0:
        lst[count-1], lst[count] = lst[count], lst[count-1]
    count += 1
print(f"result: {lst}")
