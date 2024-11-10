from typing import Any


class Pila:
    """Representa una pila con operaciones de apilar, desapilar y verificar si está vacía."""

    def __init__(self) -> None:
        """Crea una pila vacía."""
        self.items = []

    def push(self, item: Any) -> None:
        """Apila un elemento en la pila."""
        self.items.append(item)

    def pop(self) -> Any:
        """Desapila un elemento y lo devuelve.
        Si la pila está vacía, imprime un mensaje de error y retorna inmediatamente.
        """
        if self.isEmpty():
            print("La pila está vacía")
            return
        return self.items.pop()

    def isEmpty(self) -> bool:
        """Devuelve True si la pila está vacía, y False si no."""
        return self.items == []
