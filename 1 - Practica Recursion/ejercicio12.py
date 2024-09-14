# Convierta la siguiente función iterativa a una recursiva.


def iterativa(l: list[int]) -> int:
    c = 1
    for i in l:
        c = c * i
    return c


def recursiva(l: list[int]) -> int:
    if len(l) == 0:
        return 1

    return l[0] * recursiva(l[1:])


lista = [1, 5, 3]
print(iterativa(lista))
print(recursiva(lista))
