# Escriba una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

def cantidad_digitos(numero: int) -> int:
    if numero // 10 == 0:
        return 1
    
    return 1 + cantidad_digitos(numero // 10)


def cantidad_digitos_optimizado(numero: int, b: int = 1) -> int:
    if numero // 10 == 0:
        return b
    
    return cantidad_digitos_optimizado(numero // 10, b + 1)
    

print(cantidad_digitos(12312))
print(cantidad_digitos_optimizado(12312))


# Crear una función lambda para pasar a timeit
numero = 12312124124124312412345356346345234234122321314235423523523423312254657567654156498498
tiempo_funcion1 = timeit.timeit(lambda: cantidad_digitos(numero), number=10000000)
print(f"Tiempo promedio de ejecución de cantidad_digitos: {tiempo_funcion1} ms")

tiempo_funcion2 = timeit.timeit(lambda: cantidad_digitos_optimizado(numero), number=10000000)
print(f"Tiempo promedio de ejecución de cantidad_digitos_optimizado: {tiempo_funcion2} ms")

# Calcular el porcentaje de mejora
if tiempo_funcion1 > 0:
    porcentaje_mejora = ((tiempo_funcion1 - tiempo_funcion2) / tiempo_funcion1) * 100
    print(f"Porcentaje de mejora de cantidad_digitos_optimizado respecto a cantidad_digitos: {porcentaje_mejora:.2f}%")
else:
    print("El tiempo de la primera función no puede ser cero o negativo.")
