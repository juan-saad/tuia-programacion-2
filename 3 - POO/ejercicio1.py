class Point:
    """ representación de un punto en un plano cartesiano 2D """
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    

class Rectangle:

    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self) -> str:
        return '(' + str(self.width) + ', ' + str(self.height) + ', ' + str(self.corner) + ')'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        
        return self.corner == other.corner and self.height == other.height and self.width == other.width
    
    def mover_rectangulo_pura(self, dx: int, dy: int) -> 'Rectangle':
        return Rectangle(self.width, self.height, Point(self.corner.x + dx, self.corner.y + dy))

    def mover_rectangulo_modificadora(self, dx: int, dy: int):
        self.corner.x += dx
        self.corner.y += dy


punto_1 = Point(1,2)
punto_2 = Point(2,4)
punto_3 = Point(8,1)
punto_4 = Point(1,6)

rect_1 = Rectangle(1,1,punto_1)
rect_2 = Rectangle(2,1,punto_2)

rect_nueva = rect_1.mover_rectangulo_pura(2, 3)
print(rect_nueva)

rect_2.mover_rectangulo_modificadora(2,3)
print(rect_2)
