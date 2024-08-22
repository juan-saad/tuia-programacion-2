# Escriba una función recursiva que reciba 2 enteros n y b y devuelva True si n es potencia de b

def es_potencia(n: int, b: int) -> bool:
    if n == 1:
        return True
    
    if n % b != 0 or n == 0:
        return False
    
    return es_potencia(n // b, b)
    
print(es_potencia(8, 2)) # True
print(es_potencia(64, 4)) # True
print(es_potencia(70, 10)) # False
