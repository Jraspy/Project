lst_winter = (12, 1, 2)
lst_spring = (3, 4, 5)
lst_summer = (6, 7, 8)
lst_autumn = (9, 10, 11)
season = {"Winter": lst_winter, "Spring": lst_spring,
          "Summer": lst_summer, "Autumn": lst_autumn}
month = input("Enter month number [1...12]: ")
for key in season.keys():
    if int(month) in season.get(key):
        print(key)
