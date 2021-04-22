# Спортсмен занимается ежедневными пробежками.
# В первый день увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

start_distance = int(input("Enter start distance: "))
planned_distance = int(input("Enter planned distance: "))

increase_index = 0.1
count = 0
if (planned_distance - start_distance) > 0:
    increase_distance = start_distance
    while increase_distance <= planned_distance:
        increase_distance = increase_distance + increase_distance * increase_index
        count += 1
        # print(f"Day {count}: {increase_distance}")
print(f"Planned distance will come after {count} day(s)")
