class Stationery:
    def __init__(self, title="Предмет"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} карандашом")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} маркером")

our_stat = Stationery()
out_stat.draw()
our_pen = Pen("Centropen")
our_pen.draw()
our_pencil = Pencil("Erich Krause")
our_pencil.draw()
our_handle = Handle("Marker")
our_handle.draw()


