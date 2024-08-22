def f(n: int, d: int) -> None:
    if n > 1:
        if n % d == 0:
            print(d)
            f(n // d, d)
        else:
            f(n, d + 1)

def f_iter(n: int, d: int) -> None:
    while n > 1:
        if n % d == 0:
            print(d)
            n = n // d
        else:
            d = d + 1

f(30, 2)
print('\nAca empieza la funcion iterativa....\n')
f_iter(30, 2)
