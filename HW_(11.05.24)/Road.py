class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def counting_weight_of_road(self, weight, height):
        result = self._length * self._width * weight * height // 1000
        return f'{result} т'


road_1 = Road(20, 5000)
print(road_1.counting_weight_of_road(25, 5))
