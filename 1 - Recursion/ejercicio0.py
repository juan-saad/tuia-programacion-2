def factorial(n: int) -> int:
    # No existe la operacion de factorial sobre numeros negativos.
    if n < 0:
        return None

    # Caso base: n entero = 0 Devuelve: 1
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(6))
print(factorial(-2))
