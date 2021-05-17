# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
from abc import ABC, abstractmethod


class BrokenDevice(Exception):
    def __init__(self, txt):
        self.txt = f"{txt} Устройство не исправно!"


class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, name, inventory_number):
        self.name = name
        self._is_broken = False
        self.inventory_number = inventory_number
        self.is_on_warehouse = True
        self._is_enable = False

    def get_is_broken(self):
        return self._is_broken

    def get_state(self):
        return self._is_enable

    def broken(self):
        print("Устройство сломалось!")
        self._is_broken = True

    def connect_to_work_space(self, work_space):
        if self.is_on_warehouse:
            if not self._is_broken:
                print(f"Подключено на рабочем месте {work_space}")
                self.is_on_warehouse = False
            else:
                raise BrokenDevice("Ошибка подключения к рабочему месту")
        else:
            print("Нечего подключать: устройство отсутствует на складе")

    def move_to_warehouse(self):
        if self.is_on_warehouse:
            print("Устройство уже на складе!")
        else:
            print("Перемещаем на склад")
            self.is_on_warehouse = True

    def turn_on(self):
        if not self._is_broken:
            if not self._is_enable:
                self._is_enable = True
            else:
                print("Уже включено")
        else:
            raise BrokenDevice("Ошибка включения")

    def turn_off(self):
        if self._is_enable:
            self._is_enable = False
        else:
            print("Уже выключено")

    def device_repair(self):
        if self._is_broken:
            self.turn_off()
            print("Ремонтируем устройство")
            self._is_broken = False
        else:
            print("Устройсто исправно!")

    @abstractmethod
    def working(self, *kwarg):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, inv_number, printer_type):
        super().__init__(name, inv_number)
        self.printer_type = printer_type
        self._paper_count = 0
        self.printing_speed = self._get_printing_speed()
        self._cartridge_capacity = 0

    def _get_printing_speed(self):
        print("Вычисляем скорость распечатки, листв в минуту")
        return 500

    def working(self):
        if self._is_enable and not self.is_error_paper:
            print("Принтер печатает...")

    def print_test_page(self):
        if not self.is_error_paper:
            print("Распечатка тестовой страницы")

    def is_error_paper(self):
        return True if self._paper_count <= 0 else False

    def paper_load(self, paper_count):
        self._paper_count += paper_count
        print("Бумага загружена")

    def cartridge_reload(self, cartridge_capacity):
        print("Перезаправляем картридж")
        self._cartridge_capacity = cartridge_capacity

class Scanner(OfficeEquipment):

    def working(self, input_doc):
        print("Сканер сканирует...")
        return input_doc

    def send_to_email(self):
        print("Отправляем скан на почту...")


class Xerox(OfficeEquipment):

    def working(self, input_doc, copy_count):
        print(f"Ксерокс делает копию, {copy_count}шт....")
        return input_doc