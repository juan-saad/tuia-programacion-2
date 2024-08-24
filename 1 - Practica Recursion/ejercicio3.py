"""
La funcion misterio va a devolver el mismo valor de entrada de forma recursiva.
"""

def misterio(a: int) -> int:
    if a == 0:
        return a

    return 1 + misterio(a - 1)


print(misterio(1))
print(misterio(2))
print(misterio(3))
print(misterio(4))
print(misterio(5))