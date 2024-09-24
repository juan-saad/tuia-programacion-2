class Robot:
    def __init__(self, X: int = 0, Y: int = 0) -> None:
        self.X = X
        self.Y = Y

    def mueve(self, orden: str):
        if orden == "D":
            self.X += 1
        elif orden == "I":
            self.X -= 1
        elif orden == "R":
            self.Y -= 1
        elif orden == "A":
            self.Y += 1
        else:
            print(orden + " movimiento inválido")
    
    def mover_secuencias(self, ordenes: str):
        for orden in ordenes:
            self.mueve(orden)
    
    def obtener_historico_de_movimientos():
        pass

    def posicion_actual(self):
        return self.X, self.Y

mi_robot = Robot()
# orden = input("Introduce la orden: ")
# while orden != 'fin':
#     mi_robot.mueve(orden)
#     print(mi_robot.posicion_actual())
#     orden = input("Introduce la orden: ")

mi_robot.mover_secuencias("RIIDZAIA")
print(mi_robot.posicion_actual())

