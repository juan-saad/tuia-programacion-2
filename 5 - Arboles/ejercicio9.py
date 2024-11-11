class Tree:
    def __init__(self, cargo, left: "Tree" = None, right: "Tree" = None):
        self.cargo = cargo
        self.left = left
        self.right = right

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


class BST(Tree):
    def __init__(self, cargo, left: "BST" = None, right: "BST" = None):
        super().__init__(cargo, left, right)

    def insertar(self, elemento) -> None:
        if self.cargo < elemento:
            if self.left:
                self.left.insertar(elemento)
            else:
                self.left = BST(elemento)

        if self.cargo > elemento:
            if self.right:
                self.right.insertar(elemento)
            else:
                self.right = BST(elemento)


root = BST(30)

root.insertar(5)
root.insertar(25)

print(root.inorden())
