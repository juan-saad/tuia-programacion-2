class Automovil:
    def __init__(self, patente: str, marca: str, km: float = 0, litros: float = 0) -> None:
        self.patente = patente
        self.marca = marca
        self.km = km
        self.litros = litros

    def avanzar(self, km_a_recorrer: float):
        if((self.litros - (km_a_recorrer * 8.8)/100) < 0):
            print("Es necesario cargar nafta para recorrer la cantidad indicada de kilómetros")
        else:
            self.litros -= (km_a_recorrer * 8.8)/100
            self.km += km_a_recorrer

    def cargar_nafta(self, litros_introducidos: float):
        self.litros += litros_introducidos

auto = Automovil("AEF-202", "Peugeot")
auto.cargar_nafta(10)
print(auto.km) # Debería mostrar 0
print(auto.litros) # Debería mostrar 10
auto.avanzar(50)
print(auto.km) # Debería mostrar 50
print(auto.litros) # Debería mostrar 5.6
auto.avanzar(100) # Debería mostrar un mensaje de error: "nafta insuficiente"
auto.avanzar(40)
print(auto.km) # Debería mostrar 90
print(auto.litros) # Debería mostrar 2.08

