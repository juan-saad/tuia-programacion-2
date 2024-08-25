# Escriba una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

def cantidad_digitos(numero: int) -> int:
    if numero // 10 == 0:
        return 1
    
    return 1 + cantidad_digitos(numero // 10)

print(cantidad_digitos(12312))
