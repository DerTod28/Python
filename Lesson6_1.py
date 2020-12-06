import time

class TrafficLight:
    __color = "Цвет"

    def running(self):
        while True:
            print("Сейчас горит красный цвет. Остановись!")
            time.sleep(7)
            print("Подождите...Сейчас горит желтый цвет")
            time.sleep(3)
            print("Сейчас горит зеленый цвет. Можете идти.")
            time.sleep(7)
            print("Подождите...Сейчас горит желтый цвет")
            time.sleep(3)

Svetofor = TrafficLight()
Svetofor.running()
