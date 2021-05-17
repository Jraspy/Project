# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name = str
    surname = str
    position = str
    _income = {"wage": int, "bonus": int}

    def set_income(self, wage, bonus):
        self._income.clear()
        self._income.update({"wage": wage, "bonus": bonus})

    def get_income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self.get_income().setdefault("wage") + self.get_income().setdefault("bonus")


position = Position()
position.name = "Иван"
position.surname = "Сидоров"
position.position = "Инженер"
position.set_income(1000, 30)
print(position.get_full_name())
print(position.get_total_income())

# Output:
# Сидоров Иван
# 1030
#
# Process finished with exit code 0
