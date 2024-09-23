"""
1. Escriba una función recursiva repite_hola que reciba como parámetro un número entero n y
escriba por pantalla n veces el mensaje "Hola". Invóquela con distintos valores de n.
2. Escriba otra función repite_hola que reciba como parámetro un número entero n y devuelva la
cadena formada por n concatenaciones de "Hola". Invóquela con distintos valores de n.
"""


def repite_hola(n: int):
    if n <= 0:
        return ""

    print("Hola")
    repite_hola(n - 1)


def concatena_hola(n: int) -> str:
    if n <= 0:
        return ""
    else:
        return "Hola " + concatena_hola(n - 1)


print(concatena_hola(2))
print("\n")
repite_hola(5)
