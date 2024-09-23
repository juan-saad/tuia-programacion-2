def mystery(a: int, b: int) -> int:
    """multiplica el valor de a por 2, b veces
    """
    if (b == 0):
        return a
    return mystery(2 * a, b - 1)

result = mystery(3, 3)
print(result)
