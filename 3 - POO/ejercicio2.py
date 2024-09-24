from math import sqrt


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distancia(self, p2: 'Point') -> float:
        return sqrt(((p2.x - self.x) ** 2) + ((p2.y - self.y) ** 2))
    
punto_1 = Point(1,2)
punto_2 = Point(3,4)

print(punto_1.distancia(punto_2))