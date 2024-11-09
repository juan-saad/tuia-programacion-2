from typing import Any


class _Nodo:
    def __init__(self, cargo: Any = None, next: "_Nodo" = None, prev: "_Nodo" = None):
        self.cargo = cargo
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.cargo)


class ListaDoblementeEnlazada:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.len = 0

    def append(self, elem: Any) -> None:
        nuevo = _Nodo(elem)

        if not self.first:
            self.first = nuevo
        else:
            actual = self.last
            actual.next = nuevo
            nuevo.prev = actual

        self.last = nuevo
        self.len += 1
        return

    def insert(self, i: int, elem: Any) -> None:
        if i < 0 or i > self.len:
            print("Posición inválida")
            return

        nodo = _Nodo(elem)

        if i == 0:
            if self.first is None:
                self.first = nodo
                self.last = nodo
            else:
                nodo.next = self.first
                self.first.prev = nodo
                self.first = nodo

        elif i == self.len:
            if self.last is None:  # Lista vacía
                self.first = nodo
                self.last = nodo
            else:
                nodo.prev = self.last
                self.last.next = nodo
                self.last = nodo
        else:
            actual = self.first
            for _ in range(i - 1):
                actual = actual.next

            nodo.next = actual.next
            nodo.prev = actual
            actual.next.prev = nodo
            actual.next = nodo

        self.len += 1
        return

    def remove(self, elem: Any) -> None:
        if self.len == 0:
            print("La lista está vacía")
            return

        if self.first.cargo == elem:
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
                self.first.prev = None

            self.len -= 1
            return

        if self.last.cargo == elem:
            self.last = self.last.prev
            self.last.next = None
            self.len -= 1
            return

        actual = self.first
        while actual and actual.cargo != elem:
            actual = actual.next

        if actual:
            actual.prev.next = actual.next
            if actual.next:
                actual.next.prev = actual.prev
            self.len -= 1
        else:
            print("El valor no fue encontrado")

    def pop(self, i: int | None = None) -> Any:
        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            print("Posición inválida")
            return

        elem = None

        if i == 0:
            elem = self.first.cargo

            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
                self.first.prev = None

            self.len -= 1
            return elem

        if i == self.len - 1:
            elem = self.last.cargo

            self.last = self.last.prev
            self.last.next = None

            self.len -= 1
            return elem

        actual = self.first
        for _ in range(1, i):
            actual = actual.next

        if actual:
            elem = actual.cargo

            if actual.prev:
                actual.prev.next = actual.next
            if actual.next:
                actual.next.prev = actual.prev

            self.len -= 1

            return elem

        return elem

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        actual = self.first
        resultado = "["

        while actual is not None:
            resultado += str(actual.cargo)
            if actual.next is not None:
                resultado += ", "
            actual = actual.next

        resultado += "]"
        return resultado


lista_enlazada = ListaDoblementeEnlazada()

lista_enlazada.append(1)
lista_enlazada.append(4)
lista_enlazada.append(2)
lista_enlazada.append(5)
lista_enlazada.append(3)

print(lista_enlazada)

print(lista_enlazada.pop())
print(lista_enlazada.pop(0))

print(lista_enlazada)
