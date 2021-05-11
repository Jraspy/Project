# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _asfalt_weight = 25
    _asfalt_layer = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        return self._length * self._width * self._asfalt_weight * self._asfalt_layer


road1 = Road(20, 5)
print(road1.weight())


# Output:
# 12500
#
# Process finished with exit code 0
