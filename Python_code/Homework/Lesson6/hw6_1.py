# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    colors_wait_list = {"Красный": 7, "Желтый": 2, "Зеленый": 5}
    directions = {"to_green": 1, "to_red": -1, "standby": 0}
    _colors_lst = list(colors_wait_list.keys())
    _directions_lst = list(directions.values())

    def __init__(self, is_standby=False):
        if is_standby:
            self.current_color = self._colors_lst[1]
            self.direction = self._directions_lst[::-1][0]
        else:
            self.current_color = self._colors_lst[0]
            self.direction = self._directions_lst[0]

    def running(self, count):
        if count > 0:
            i = 0
            while i != count:
                self.traffic_light_show_current()
                self._set_next_light()
                i += 1
        else:
            print("Светофор без электричества")

    def _set_next_light(self):
        current_position = self._colors_lst.index(self.current_color)
        temp = current_position + self.direction
        if (temp < 0) or (temp > len(self._colors_lst)-1):
            self.direction = self.direction * (-1)
        next_position = current_position + self.direction
        self.current_color = self._colors_lst[next_position]

    def traffic_light_show_current(self):
        color = self.current_color
        print(f"Цвет сфетофора: {color}. Задержка: {TrafficLight.colors_wait_list[color]} сек")
        time.sleep(TrafficLight.colors_wait_list[color])


print("Светофор в боевом режиме")
traffic_light = TrafficLight()
traffic_light.running(10)
print("Светофор в дежурном режиме")
traffic_light_standby = TrafficLight(True)
traffic_light_standby.running(3)
print("Светофоротключен")
traffic_light_standby = TrafficLight()
traffic_light_standby.running(-1)


# Output:
# Светофор в боевом режиме
# Цвет сфетофора: Красный. Задержка: 7 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Цвет сфетофора: Зеленый. Задержка: 5 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Цвет сфетофора: Красный. Задержка: 7 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Цвет сфетофора: Зеленый. Задержка: 5 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Цвет сфетофора: Красный. Задержка: 7 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Светофор в дежурном режиме
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Цвет сфетофора: Желтый. Задержка: 2 сек
# Светофоротключен
# Светофор без электричества
#
# Process finished with exit code 0
