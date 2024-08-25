# Escriba una función recursiva que calcule el n-ésimo número triangular (el número 1 + 2 + 3 + ... + n).


def numero_triangular(n: int) -> int:
    # Caso base 1: Por definicion, el nro triangular es la suma de los n numeros naturales de 1 a n.
    if n <= 0:
        return 0

    # Caso base 2: si n = 1, T1 = 1
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n - 1)


print(numero_triangular(1))
print(numero_triangular(3))
print(numero_triangular(6))
print(numero_triangular(-1))
print(numero_triangular(0))
