# Escriba una función potencia(b,n) que calcule la potencia para cualquier n entero, incluso si n es negativa. Utilice una función auxiliar.

from fractions import Fraction

def _potencia(base: float, exponente: int) -> float:
    if base == 0:
        return 0

    if exponente == 0:
        return 1
    
    return base * _potencia(base, exponente - 1)


def potencia(base: float, exponente: int) -> float:
    if base == 0 and exponente == 0:
        raise ValueError("La operación 0^0 es indeterminada en el análisis matemático.")
    
    if exponente < 0:
        return 1 / _potencia(base, -exponente)
    else: 
        return _potencia(base, exponente)


base = 5
exponente = -19

print(Fraction(potencia(base, exponente)))
