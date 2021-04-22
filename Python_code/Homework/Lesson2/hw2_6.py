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
