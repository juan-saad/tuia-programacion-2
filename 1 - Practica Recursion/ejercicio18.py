def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_dicc(n: int, valores: dict = {}) -> int:
    if n == 0 or n == 1:
        valores[n] = n
        return n

    if valores.get(n):
        return valores[n]

    if not valores.get(n):
        valores[n] = fibonacci_dicc(n - 1, valores) + fibonacci_dicc(n - 2, valores)

    return valores[n]


print(fibonacci_dicc(5))
