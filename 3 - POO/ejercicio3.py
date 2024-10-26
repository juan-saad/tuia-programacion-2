class Automovil:
    CONSUMO_POR_100KM = 8.8  # Consumo en litros cada 100 km

    def __init__(
        self, patente: str, marca: str, km: float = 0, litros: float = 0
    ) -> None:
        if km < 0 or litros < 0:
            raise ValueError(
                "Los kilómetros y litros iniciales no pueden ser negativos."
            )
        self.patente = patente
        self.marca = marca
        self.km = km
        self.litros = litros

    def avanzar(self, km_a_recorrer: float) -> bool:
        if km_a_recorrer < 0:
            print("No se pueden recorrer kilómetros negativos.")
            return False

        consumo_necesario = (km_a_recorrer * self.CONSUMO_POR_100KM) / 100
        if consumo_necesario > self.litros:
            print(
                f"Faltan {consumo_necesario - self.litros:.2f} litros para recorrer {km_a_recorrer} km."
            )
            return False

        self.litros -= consumo_necesario
        self.km += km_a_recorrer
        return True

    def cargar_nafta(self, litros_introducidos: float) -> bool:
        if litros_introducidos < 0:
            print("No se pueden cargar litros negativos.")
            return False
        self.litros += litros_introducidos
        return True

    def __str__(self) -> str:
        return f"Automóvil {self.marca} ({self.patente}) - KM: {self.km}, Litros: {self.litros:.2f}"


# Ejemplo de uso
auto = Automovil("AEF-202", "Peugeot")
print(auto)  # Automóvil Peugeot (AEF-202) - KM: 0, Litros: 0.00

auto.cargar_nafta(10)
print(auto)  # Automóvil Peugeot (AEF-202) - KM: 0, Litros: 10.00

auto.avanzar(50)  # Avanza 50 km
print(auto)  # Automóvil Peugeot (AEF-202) - KM: 50, Litros: 5.60

auto.avanzar(100)  # Muestra mensaje: "Faltan X litros..."
auto.avanzar(40)  # Avanza 40 km más
print(auto)  # Automóvil Peugeot (AEF-202) - KM: 90, Litros: 2.08
