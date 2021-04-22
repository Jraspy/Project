# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

usr_count = int(input("Введите кол-во товаров: "))
product_Name = "название"
product_Price = "цена"
product_Count = "количество"
product_Unit = "ед"
analysis_list = {product_Name: [], product_Price: [],
                 product_Count: [], product_Unit: []}
products_list = []
i = 1
while i <= usr_count:
    name = input(f"Enter {product_Name}: ")
    price = int(input(f"Enter {product_Price}: "))
    product_count = int(input(f"Enter {product_Count}: "))
    unit = input(f"Enter {product_Unit}: ")
    product_params = {product_Name: name, product_Price: price,
                      product_Count: product_count, product_Unit: unit}
    products_tuple = (i, product_params)
    products_list.append(products_tuple)
    i += 1
result_dict = {}
for key in analysis_list:
    temp_list = []
    for position in products_list:
        characteristics = position[1]
        temp_list.append(characteristics.get(key))
    result_dict.update({key: set(temp_list)})
print(result_dict)
