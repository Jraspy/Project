# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
from abc import ABC, abstractmethod


class BrokenDevice(Exception):
    def __init__(self, txt):
        self.txt = f"{txt} Устройство не исправно!"


class Warehouse:
    def __init__(self, *devices):
        self.storage = list(devices)

    def get_storage(self):
        return self.storage

    def take_to_storage(self, *devices):
        for device in devices:
            device.is_on_warehouse = True
            self.storage.append(device)
            print(f"'{device.name}' перемещено на склад")

    def send_from_storage(self, *devices):
        for device in devices:
            if self.storage.count(device) > 0:
                device.is_on_warehouse = False
                self.storage.remove(device)
                print(f"'{device.name}' передано со склада")
            else:
                print("Устройство на складе не обнаружено")


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
        return 500

    def working(self):
        if self._is_enable and self._paper_count > 0:
            print("Принтер печатает...")
        else:
            print("Бумага отсутствует")

    def print_test_page(self):
        if self._paper_count > 0:
            print("Распечатка тестовой страницы")
            self._paper_count -= 1
        else:
            print("Бумага отсутствует")

    def paper_load(self, paper_count=200):
        self._paper_count += paper_count
        print(f"Бумага загружена, в лотке {self._paper_count} листов")

    def cartridge_reload(self, cartridge_capacity=500):
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

printer1 = Printer("Принтер1", 1, "Струйный")
warehouse = Warehouse()
warehouse.take_to_storage(printer1)
print(f"Название первого элемента в хранилище: {warehouse.get_storage()[0].name}")
warehouse.send_from_storage(printer1)
printer1.cartridge_reload()
printer1.paper_load()
printer1.turn_on()
printer1.print_test_page()
printer1.working()

# Output:
# 'Принтер1' перемещено на склад
# Название первого элемента в хранилище: Принтер1
# 'Принтер1' передано со склада
# Перезаправляем картридж
# Бумага загружена, в лотке 200 листов
# Распечатка тестовой страницы
# Принтер печатает...
#
# Process finished with exit code 0
