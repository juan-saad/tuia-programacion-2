class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def preorden(self):
        """Recorrido en preorden: Nodo, Izquierda, Derecha"""
        print(f'{self.cargo},', end=" ")
        if self.left:
            self.left.preorden()
        if self.right:
            self.right.preorden()
            
    def inorden(self):
        """Recorrido en inorden: Izquierda, Nodo, Derecha"""
        if self.left:
            self.left.inorden()
        print(self.cargo, end=" ")
        if self.right:
            self.right.inorden()
        
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
