user_str = input("Enter the string: ")
for ind, each_str in enumerate(user_str.split(" ")):
    print(f"{ind}. {each_str[0:10]}")
