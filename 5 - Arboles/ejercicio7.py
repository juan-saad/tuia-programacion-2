from typing import Any


class Tree:
    def __init__(self, cargo: Any, left: "Tree" = None, right: "Tree" = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def search(self, elem: Any) -> bool:
        if self.cargo == elem:
            return True

        if self.left and self.left.search(elem):
            return True

        if self.right and self.right.search(elem):
            return True

        return False

    def height(self) -> int:
        if not self:
            return -1

        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1

        return 1 + max(left_height, right_height)

    def preorden(self):
        """Recorrido en preorden: Nodo, Izquierda, Derecha"""
        resultado = [self.cargo]  # Primero, agregar el nodo actual.

        if self.left:
            resultado.extend(self.left.preorden())  # Recursión al subárbol izquierdo
        if self.right:
            resultado.extend(self.right.preorden())  # Recursión al subárbol derecho

        return resultado

    def inorden(self):
        """Recorrido en inorden: Izquierda, Nodo, Derecha"""
        resultado = []

        if self.left:
            resultado.extend(self.left.inorden())  # Recursión al subárbol izquierdo
        resultado.append(self.cargo)  # Luego, agregar el nodo actual.
        if self.right:
            resultado.extend(self.right.inorden())  # Recursión al subárbol derecho

        return resultado

    def postorden(self):
        """Recorrido en postorden: Izquierda, Derecha, Nodo"""
        resultado = []

        if self.left:
            resultado.extend(self.left.postorden())  # Recursión al subárbol izquierdo
        if self.right:
            resultado.extend(self.right.postorden())  # Recursión al subárbol derecho
        resultado.append(self.cargo)  # Finalmente, agregar el nodo actual.

        return resultado

    def __str__(self) -> str:
        return str(self.cargo)


def sumatoria_especial(
    tree: "Tree",
    max_level: int = 0,
    start: int = 0,
    end: int = 0,
    current_level: int = 0,
) -> int:
    # Caso base: Si el árbol está vacío o hemos superado el nivel máximo permitido
    if tree is None or current_level > max_level:
        return 0

    # Valor del nodo actual si está en el rango
    node_value = tree.cargo if start <= tree.cargo <= end else 0

    left_sum = sumatoria_especial(tree.left, max_level, start, end, current_level + 1)
    right_sum = sumatoria_especial(tree.right, max_level, start, end, current_level + 1)

    # Retorna la suma del nodo actual y las sumas de los subárboles
    return node_value + left_sum + right_sum


tree = Tree(
    10,
    Tree(5, Tree(2), Tree(7, Tree(30, None, Tree(1, None, Tree(100))))),
    Tree(15, Tree(12, None, Tree(20)), Tree(18)),
)

print(sumatoria_especial(tree, 25, 0, 15))