# Escriba una función recursiva que encuentre el mayor elemento de una lista.


def mayor_elemento(lista: list[int]) -> int:
    # Caso base: si la lista tiene un solo elemento, ese es el mayor
    if len(lista) == 1:
        return lista[0]

    # Paso recursivo: comparar el primer elemento con el mayor del resto de la lista
    max_rest = mayor_elemento(lista[1:])
    return lista[0] if lista[0] > max_rest else max_rest


lista = [1, 5, 3, 6, 2, -2, -3, -6, 2, 4, 8, 9, 10, 11, -10, -2, -12]

print(mayor_elemento(lista))
