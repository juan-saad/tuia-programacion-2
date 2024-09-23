# Escribir una función recursiva que reciba como parámetros dos cadenas a y b, y encuentre la posición
# de la primer ocurrencia de b como subcadena de a.
# Ejemplo:
# - posicion_de("Un tete a tete con Tete", "te") -> 3
# - posicion_de("Un tete a tete con Tete", "Te") -> 19
# Ayuda: Puede ser de utilidad el método de str.startswith que nos dice si una cadena empieza con
# una subcadena dada. Puede leer más sobre este método en la documentación oficial.


def posicion_de(a: str, b: str, c=0) -> int:
    if len(a) == 0 or len(b) == 0 or len(b) > len(a):
        return -1

    if a.startswith(b):
        return c
    
    return posicion_de(a[1:], b, c + 1)


palabra = "Un tete a tete con Tete"

print(posicion_de(palabra, "te"))
print(posicion_de(palabra, "Te"))
