# Ya sabemos que la implementación recursiva del cálculo del número de Fibonacci F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2)
# es ineficiente porque muchas de las ramas calculan reiteradamente los mismos valores.
# Escriba una función fibonacci(n) que calcule el n-ésimo número de Fibonacci de forma recursiva, pero que utilice un diccionario
# para almacenar los valores ya computados y no computarlos más de una vez.
# Nota: Será necesario implementar una función wrapper para cumplir con la signatura de la función pedida.


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
