# Escriba una función recursiva que reciba 2 enteros n y b y devuelva True si n es potencia de b

def es_potencia(n: int, b: int) -> bool:
    # Caso base 1: Si n es 0 o b es 0, no es potencia.
    if n == 0 or b == 0:
        return False
    
    # Caso base 2: Si n es 1, es una potencia de b (b^0 = 1).
    if n == 1:
        return True
    
    # Caso base 3: Si n no es divisible por b, no puede ser potencia.
    if n % b != 0:
        return False
    
    return es_potencia(n // b, b)

print(es_potencia(1, 1))        # True => porque 1^0 = 1
print(es_potencia(1, -1))       # True => porque (-1)^0 = 1
print(es_potencia(-1, -1))      # True => porque (-1)^1 = -1    
print(es_potencia(8, 2))        # True => 2^3 = 8
print(es_potencia(-8, -2))      # True => (-2)^3 = -8
print(es_potencia(64, 4))       # True => 4^3 = 64
print(es_potencia(9, -3))       # True => (-3)^3 = -9
print(es_potencia(-8, 2))       # False => 2^3 = 8
print(es_potencia(8, -2))       # False => (-2)^3 = -8
print(es_potencia(70, 10))      # False => 10^2 = 100
print(es_potencia(1, 0))        # False => 0^k no existe k como solucion
print(es_potencia(0, 1))        # False => 1^k no existe k como solucion