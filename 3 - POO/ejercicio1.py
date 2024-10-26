from math import sqrt
import random


class Point:
    """representación de un punto en un plano cartesiano 2D"""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def eucledian_distance(self, other: "Point") -> float:
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)


class Rectangle:
    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

    def mover_rectángulo_pura(self, dx: int, dy: int) -> "Rectangle":
        return Rectangle(
            self.width, self.height, Point(self.corner.x + dx, self.corner.y + dy)
        )

    def mover_rectángulo_modificadora(self, dx: int, dy: int) -> None:
        self.corner.x += dx
        self.corner.y += dy

    def __str__(self) -> str:
        return f"({self.width}, {self.height}, {self.corner})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False

        return (self.width, self.height, self.corner) == (
            other.width,
            other.height,
            other.corner,
        )


rectangulos = [Rectangle]

# --- Crear instancias y almacenarlas ---
for _ in range(5):  # Crear 5 instancias
    # Generar valores aleatorios para el punto y el rectángulo
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    width = random.randint(1, 20)
    height = random.randint(1, 20)

    # Crear punto y rectángulo
    punto = Point(x, y)
    rectángulo = Rectangle(width, height, punto)

    # Guardar en la lista
    rectangulos.append(rectángulo)

print(rectangulos[2])
print(rectangulos[2].mover_rectángulo_pura(1, -2))

print(rectangulos[3])
rectangulos[3].mover_rectángulo_modificadora(3, -1)
print(rectangulos[3])
