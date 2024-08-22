def recursiva(t: int, k: int) -> int:
    if t >= 100:
        return (t, k)
    else:
        return recursiva(t + k, k + 1)

def recursiva_iterativa(t: int, k: int) -> int:
    while t < 100:
        t = t + k
        k += 1

    return (t, k)

t = 15
k = 1

print(recursiva(t, k))
print('\nAca empieza la funcion iterativa....\n')
print(recursiva_iterativa(t, k))
