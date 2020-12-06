class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def asphalt_counting(self):
        asphalt_mass = 25
        width_of_cover = 5
        total = self._length * self._width * asphalt_mass * width_of_cover
        print(f"Масса асфальта составляет {total/1000} тонн.")


road = Road(20, 5000)
road.asphalt_counting()



