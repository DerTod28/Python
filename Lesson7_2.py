from abc import ABC
from abc import abstractmethod
import math


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def rashod_materialov(self):
        pass

    def __add__(self, other):
        return self.param + other.param

class Coat(Clothes):
    @property
    def rashod_materialov(self):
        print(f"Для пошива пальто нам будет необходимо {(self.param / 6.5) + 0.5:.2f}")
        return math.ceil((self.param / 6.5) + 0.5)

class Costume(Clothes):
    @property
    def rashod_materialov(self):
        print(f"Для пошива костюма нам будет необходимо {(2 * self.param + 0.3)}")
        return math.ceil((2 * self.param + 0.3))

coat = Coat(int(input("Введите размер пальто: ")))
print(f'Потребуется приблитительно {coat.rashod_materialov} метров ткани')
costume = Costume(int(input("Введите рост заказчика: ")))
print(f'Потребуется приблитительно {costume.rashod_materialov} метров ткани')
print(f'Всего нам потребуется {coat.rashod_materialov + costume.rashod_materialov} метров ткани')