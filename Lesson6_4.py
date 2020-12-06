import random
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool
        # print(f"{speed}, {color}, {name}, {is_police}")

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn_left_right(self):
        directions = ['налево', 'направо']
        print("Машина повернула", random.choice(directions))

    def show_speed(self):
        print("Текущая скорость автомобиля -", self.speed)

class TownCar(Car):
    def town_car(self):
        print("Это городская машина")
        if self.speed > 60:
            Car.stop()
            print("Вы превысили скорость")

class SportCar(Car):
    def sport_car(self):
        print("Это спортивная машина")

class WorkCar(Car):
    def work_car(self):
        print("Это рабочая машина")
        if self.speed > 40:
            Car.stop(self)
            print("Вы превысили скорость")

class Police(Car):
    def police_car(self):
        print("Это полицеская машина")


my_car_1 = TownCar(30, "желтая", "Auto", False)
my_car_1.town_car()
my_car_1.go()
my_car_1.turn_left_right()
my_car_1.show_speed()
my_car_1.stop()

my_car_2 = SportCar(120, "розовая", "BMW", False)
my_car_2.sport_car()
my_car_2.go()
my_car_2.turn_left_right()
my_car_2.show_speed()
my_car_2.stop()

my_car_3 = WorkCar(50, "черная", "Лимузин", False)
my_car_3.work_car()
my_car_3.go()
my_car_3.turn_left_right()
my_car_3.show_speed()
my_car_3.stop()

my_car_4 = Police(60, "синяя", "Honda", True)
my_car_4.police_car()
my_car_4.go()
my_car_4.turn_left_right()
my_car_4.show_speed()
my_car_4.stop()
