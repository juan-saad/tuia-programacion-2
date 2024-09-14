# Escriba una función que tome una lista y devuelva esa misma lista en orden inverso. Realice dos versiones:
# - reversaR que resuelva utilizando recursión.
# - reversaI que resuelva utilizando iteración.
# Nota: No utilice la función built-in reversed en su solución, ni el método reversed.


def reversa_recursiva(lista: list) -> list:
    if len(lista) <= 1:
        return lista

    return [lista[len(lista) - 1]] + reversa_recursiva(lista[:-1])


def reversa_iterativa(lista: list) -> list:
    reversa = []

    for i in range(len(lista) - 1, -1, -1):
        reversa.append(lista[i])

    return reversa


lista = [1, 2, 3, 4, 5, 6]


print(reversa_iterativa(lista))
print(reversa_recursiva(lista))
