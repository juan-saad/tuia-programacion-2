### Escriba una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo:
### replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])


def replicar(lista: list[int], n: int) -> list[int]:
    if len(lista) == 0 or n == 0:
        return []

    if n == 1:
        return lista

    return [lista[0]] * n + replicar(lista[1:], n)


lista = [1, 3, 3, 7]

print(replicar(lista, 2))
