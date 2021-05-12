# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self):
        return self.size/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        return 2*self.height + 0.3


coat = Coat(10)
print(f"Расход ткани на пальто: {coat.consumption}")
costume = Costume(20)
print(f"Расход ткани на костюм: {costume.consumption}")
print(f"Общий расход: {coat.consumption + costume.consumption}")

# Output:
# Расход ткани на пальто: 2.0384615384615383
# Расход ткани на костюм: 40.3
# Общий расход: 42.33846153846154
#
# Process finished with exit code 0
