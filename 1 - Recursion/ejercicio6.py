# Escriba una función recursiva que tome un numero natural n e imprima todos los números desde n hasta 1.

def serie_numeros(n: int) -> None:
    if n <= 0:
        return ""

    print(str(n))
    serie_numeros(n - 1)

serie_numeros(5)