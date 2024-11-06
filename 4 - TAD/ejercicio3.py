from typing import Any


class _Nodo:
    def __init__(self, dato: Any = None, prox: "_Nodo" = None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


class ListaEnlazada:
    """Modela una lista enlazada."""

    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len = 0

    def insert(self, i: int, x: Any) -> None:
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """
        if i < 0 or i > self.len:
            print("Posición inválida")
            return
        nuevo = _Nodo(x)
        if i == 0:
            # Caso particular : insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for _ in range(1, i):
                n_ant = n_ant.prox
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def append(self, x: Any) -> None:
        """Agrega el elemento x al final de la lista."""
        nuevo = _Nodo(x)
        if self.prim is None:
            self.prim = nuevo
        else:
            actual = self.prim
            while actual.prox is not None:
                actual = actual.prox
            actual.prox = nuevo
        self.len += 1

    def pop(self, i: int | None = None) -> Any:
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se
        retorna inmediatamente. Si no se recibe la posición, devuelve el
        último elemento.
        """
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            print("Posición inválida")
            return
        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i -1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for _ in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
        self.len -= 1
        return dato

    def remove(self, x: Any) -> None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if self.len == 0:
            print("La lista está vacía")
            return
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act is None:
                print("El valor no está en la lista.")
                return
            # Descartar el nodo
            n_ant.prox = n_act.prox
        self.len -= 1

    def extend(self, lista: "ListaEnlazada") -> None:
        if lista.len <= 0:
            return

        ultimo = self.prim
        while ultimo.prox is not None:
            ultimo = ultimo.prox

        ultimo.prox = lista.prim

        # Actualizamos la longitud de la lista actual
        self.len += lista.len

    def remover_todos(self, elemento: Any) -> int:
        contador = 0

        if not self.prim:
            return contador

        anterior = None
        actual = self.prim

        while actual:
            if actual.dato == elemento:
                contador += 1

                # Si es el primer nodo, actualizamos el inicio de la lista
                if anterior is None:
                    self.prim = actual.prox
                else:
                    anterior.prox = actual.prox
            else:
                anterior = actual

            actual = actual.prox

        self.len -= contador
        return contador

    def __len__(self):
        return self.len

    def __str__(self) -> str:
        actual = self.prim
        resultado = "["

        while actual is not None:
            resultado += str(actual.dato)
            if actual.prox is not None:
                resultado += ", "
            actual = actual.prox

        resultado += "]"
        return resultado


def ver_lista(nodo: _Nodo | None) -> None:
    """Recorre todos los nodos a través de sus enlaces, mostrando sus
    contenidos como un array.
    """
    resultado = "["
    while nodo is not None:
        resultado += str(nodo.dato)
        if nodo.prox is not None:
            resultado += ", "
        nodo = nodo.prox
    resultado += "]"
    print(resultado)


lista_enlazada = ListaEnlazada()
lista_enlazada.append("a")
lista_enlazada.append("b")
lista_enlazada.append("a")
lista_enlazada.append("c")
lista_enlazada.append("d")
lista_enlazada.append("a")
lista_enlazada.append("a")
lista_enlazada.append("d")

print(lista_enlazada)
print(len(lista_enlazada))

lista_enlazada.remover_todos()

print(lista_enlazada)
print(len(lista_enlazada))
