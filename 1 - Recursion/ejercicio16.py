# Escriba una función recursiva que dada una cadena determine si en la misma hay más letras 'A' o letras 'E'. Utilice una función auxiliar.

from typing import Tuple


def _contar_letras(
    palabra: str, indice=0, contador_A=0, contador_E=0
) -> Tuple[int, int]:
    if indice >= len(palabra):
        return contador_A, contador_E

    if palabra[indice] == "A":
        contador_A += 1

    if palabra[indice] == "E":
        contador_E += 1

    return _contar_letras(palabra, indice + 1, contador_A, contador_E)


def contar_letras(palabra: str) -> bool:
    if len(palabra) == 0:
        return False

    cant_A, cant_E = _contar_letras(palabra)
    return cant_A > cant_E


palabra = "AAAEE"
print(contar_letras(palabra))
