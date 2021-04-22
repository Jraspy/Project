rate_list = [7, 5, 3, 3, 2]
print(rate_list)
usr_rate = int(input("Enter new rate: "))
position = 0
if usr_rate in rate_list:
    count_entry = rate_list.count(usr_rate)
    position_entry = rate_list.index(usr_rate)
    position = position_entry + count_entry
else:
    for item in rate_list:
        if usr_rate > item:
            position = rate_list.index(item)
            break
        elif usr_rate < item:
            position = rate_list.index(item) + 1
rate_list.insert(position, usr_rate)
print(rate_list)
