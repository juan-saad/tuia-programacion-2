# Escriba una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

def cantidad_digitos(numero: int) -> int:
    cantidad = 1

    if numero // 10 == 0:
        return 1
    
    cantidad += cantidad_digitos(numero // 10)
    return cantidad

print(cantidad_digitos(12312))
