class Tree:
    def __init__(self, cargo, left = None, right = None):
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

def invertir(arbol: "Tree") -> None:
    if not arbol:
        return None
    
    if arbol.left:
        invertir(arbol.left)
    if arbol.right:
        invertir(arbol.right)
        
    arbol.left, arbol.right = arbol.right, arbol.left
    
    return arbol

def sumatoria(arbol: "Tree") -> float:
    if arbol is None:
        return 0.0
    
    lsuma = sumatoria(arbol.left)
    rsuma = sumatoria(arbol.right)
    
    return arbol.cargo + lsuma + rsuma

izq1 = Tree(-1)
der1 = Tree(10)
izq2 = Tree(0)
der2 = Tree(20)

izq3 = Tree(5,izq1,der1)
der3 = Tree(3,izq2,der2)

root = Tree(1, izq3, der3)

root.inorden()
print('\n')
print(invertir(root).inorden())
print(sumatoria(root))
