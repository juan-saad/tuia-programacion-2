from typing import Any


class Tree:
    def __init__(self, cargo: Any, left: "Tree" = None, right: "Tree" = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def nodes(self) -> int:
        count = 1
        if self.left:
            count += self.left.nodes()
        if self.right:
            count += self.right.nodes()
        return count

    def min_max(self) -> tuple[Any, Any]:
        min_val = max_val = self.cargo

        if self.left:
            left_min, left_max = self.left.min_max()
            min_val = min(min_val, left_min)
            max_val = max(max_val, left_max)

        if self.right:
            right_min, right_max = self.right.min_max()
            min_val = min(min_val, right_min)
            max_val = max(max_val, right_max)

        return (min_val, max_val)

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
    
    def inorden(self) -> list:
        """Recorrido en inorden: Izquierda, Nodo, Derecha"""
        resultado = []
        
        if self.left:
            resultado.extend(self.left.inorden())  # Recursión al subárbol izquierdo
        resultado.append(self.cargo)  # Luego, agregar el nodo actual.
        if self.right:
            resultado.extend(self.right.inorden())  # Recursión al subárbol derecho
        
        return resultado


def copiar(tree: "Tree") -> "Tree":
    nuevo = Tree(tree.cargo)

    if tree.left:
        nuevo.left = copiar(tree.left)
    if tree.right:
        nuevo.right = copiar(tree.right)

    return nuevo


tree = Tree(
    10,
    Tree(5, Tree(2), Tree(7, Tree(30, None, Tree(1, None, Tree(100))))),
    Tree(15, Tree(12, None, Tree(20)), Tree(18)),
)

tree2 = copiar(tree)

print(tree.inorden())
print(tree2.inorden())
