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

    def copiar(self) -> "Tree":
        nuevo = Tree(self.cargo)

        if self.left:
            nuevo.left = self.copiar(self.left)
        if self.right:
            nuevo.right = self.copiar(self.right)

        return nuevo

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


def combinar(tree1: "BST", tree2: "BST") -> "BST":
    if tree1 and not tree2:
        return tree1

    if tree2 and not tree1:
        return tree2

    list1 = treeToList(tree1)
    list2 = treeToList(tree2)

    combinedList = recursiveMergeList(list1, list2)
    combinedTree = listToTree(combinedList)

    return combinedTree


def treeToList(tree: "BST") -> list:
    return tree.inorden()


def listToTree(list: list) -> "BST":
    if list == []:
        return None

    middle = len(list) // 2
    leftTree = listToTree(list[:middle])
    rightTree = listToTree(list[middle + 1 :])
    
    return BST(list[middle], leftTree, rightTree)


def recursiveMergeList(list1: list, list2: list) -> list:
    if list1 == []:
        return list2

    if list2 == []:
        return list1

    return (
        [list1[0]] + recursiveMergeList(list1[1:], list2)
        if list1[0] <= list2[0]
        else [list2[0]] + recursiveMergeList(list1, list2[1:])
    )


tree1 = BST(7, BST(3, BST(1), BST(4)), BST(12, BST(9)))
tree2 = BST(20, BST(8, BST(5), BST(17)), BST(30))
