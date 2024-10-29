from typing import List


class Materia:
    def __init__(
        self, codigo_materia: str, nombre: str, creditos: int, nota: float = None
    ) -> None:
        self.codigo_materia = codigo_materia
        self.nombre = nombre
        self.creditos = creditos
        self.nota = nota

    def __str__(self) -> str:
        return f"{self.codigo_materia} {self.nombre} ({self.nota})"


class Carrera:

    def promedio_carrera(self) -> str:
        if not self.materias or not any(
            materia.nota
            for materia in self.materias
            if materia.nota and materia.nota >= 6
        ):
            return "N/A"

        promedio = sum(materia.nota for materia in self.materias if materia.nota) / len(
            self.materias
        )

        return f"{promedio:.2f}"

    def aprobar(self, codigo_materia: str, nota: float) -> None:
        materia_encontrada = [
            materia
            for materia in self.materias
            if materia.codigo_materia == codigo_materia
        ]

        if materia_encontrada:
            materia_encontrada[0].nota = nota
        else:
            print(
                f"Error: La materia {codigo_materia} no es parte del plan de estudios"
            )

    def __init__(self, materias: "List[Materia]") -> None:
        self.materias = materias

    def __str__(self) -> str:
        materias_str = " ".join(
            str(materia)
            for materia in self.materias
            if materia.nota and materia.nota >= 6
        )
        
        return f"Créditos: {sum(materia.creditos for materia in self.materias)} -- Promedio: {self.promedio_carrera()} -- Materias aprobadas: {materias_str}"


analisis2 = Materia("61.03", "Análisis 2", 8)
fisica2 = Materia("62.01", "Física 2", 8)
algo1 = Materia("75.40", "Algoritmos 1", 6)
c = Carrera([analisis2, fisica2, algo1])
print(c)

c.aprobar("95.14", 7)
c.aprobar("75.40", 10)
c.aprobar("62.01", 7)
print(c)
