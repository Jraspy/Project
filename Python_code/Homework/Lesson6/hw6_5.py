# Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = str

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Рисует ручка")


class Pencil(Stationery):
    def draw(self):
        print("Рисует карандаш")


class Handle(Stationery):
    def draw(self):
        print("Рисует маркер")


stationery = Stationery()
stationery.title = "Канцелярия"
stationery.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.title = "Маркер"
handle.draw()

# Output:
# Запуск отрисовки
# Рисует ручка
# Рисует карандаш
# Рисует маркер
#
# Process finished with exit code 0