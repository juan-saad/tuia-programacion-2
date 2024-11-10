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


class PilaConMaximo(Pila):
    def __init__(self) -> None:
        super().__init__()
        
    def obtener_maximo(self) -> Any:
        if self.isEmpty():
            return
        
        max = self.items[0]
        
        for i in range(1, len(self.items)):
            elem = self.items[i]
            if elem > max:
                max = elem
        
        return max
    
pila = PilaConMaximo()

pila.push(2)
pila.push(10)
pila.push(4)
pila.push(5)

print(pila.obtener_maximo())