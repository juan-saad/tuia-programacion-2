"""
1. Escriba una función repite_saludo que reciba como parámetro un número entero n y una cadena
saludo y escriba por pantalla n veces el valor de saludo. Invóquela con distintos valores de n y
de saludo.
2. Escriba otra función repite_saludo que reciba como parámetro un número entero n y una cadena
saludo y devuelva el valor de n concatenaciones de saludo. Invóquela con distintos valores de n
y de saludo
"""

def repite_saludo(n: int, saludo: str):
    if n <= 0:
        return ""

    print(saludo + " ")
    repite_saludo(n - 1, saludo)


def concatena_saludo(n: int, saludo: str) -> str:
    if n <= 0:
        return ""
    else:
        return saludo + " " + concatena_saludo(n - 1, saludo)

# repite_saludo(2, "Hola juan")
print(concatena_saludo(3, "Hola juan"))