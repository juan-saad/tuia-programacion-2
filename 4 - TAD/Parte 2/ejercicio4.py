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

    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int:
        return len(self.items)


def validar(expresion: str) -> bool:
    pila = Pila()
    pares = {")": "(", "}": "{", "]": "["}

    for char in expresion:
        if char in "({[":
            pila.push(char)
        elif char in ")]}":
            if not pila.isEmpty() and pila.pop() != pares[char]:
                return False

    return pila.isEmpty()


print(validar("(x+y)/2"))  # -> True
print(validar("[8*4(x+y)]+{2/5}"))  # -> True
print(validar("(x+y]/2"))  # -> False
print(validar("1+)2(+3"))  # -> False
