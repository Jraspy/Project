# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    speed = int
    color = str
    name = str
    is_police = False

    def go(self):
        print("Машина поехала...")

    def stop(self):
        print("Машина остановилась...")

    def turn(self, direction):
        print(f"Машина повернула: {direction}")

    def show_speed(self):
        print(f"Скорость машины: {self.speed}")
        return self.speed


class TownCar(Car):
    _speed_limit = 60

    def show_speed(self):
        print(f"Скорость машины: {self.speed}")
        if int(self.speed) > self._speed_limit:
            print("Превышена скорость!")
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    _speed_limit = 40

    def show_speed(self):
        print(f"Скорость машины: {self.speed}")
        if int(self.speed) > self._speed_limit:
            print("Превышена скорость!")
        return self.speed


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True


reno = TownCar()
reno.speed = 50
reno.name = "Renault"
reno.color = "white"
reno.go()
reno.show_speed()
reno.turn("right")
reno.show_speed()
reno.speed = 70
reno.show_speed()

bmw = SportCar()
bmw.speed = 200
bmw.color = "Black"
bmw.name = "Boomer"
bmw.go()
bmw.turn("left")
bmw.stop()

uaz = WorkCar()
uaz.speed = 10
uaz.color = "Brown"
uaz.name = "Bobik"
uaz.go()
uaz.speed = 55
uaz.stop()

audi = PoliceCar()
audi.color = "White"
audi.speed = 120
print(audi.is_police)

# Output:
# Машина поехала...
# Скорость машины: 50
# Машина повернула: right
# Скорость машины: 50
# Скорость машины: 70
# Превышена скорость!
# Машина поехала...
# Машина повернула: left
# Машина остановилась...
# Машина поехала...
# Машина остановилась...
# True
#
# Process finished with exit code 0
