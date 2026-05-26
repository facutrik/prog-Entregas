class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes = []

    def hay_cupo(self):
        return len(self.estudiantes) < self.capacidad

    def agregar_estudiante(self, estudiante):
        if self.hay_cupo():
            self.estudiantes.append(estudiante)
            return True
        return False

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)

    def mostrar_estado(self):
        print(f"\nCurso: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Profesor: {self.profesor}")
        print(f"Inscriptos: {len(self.estudiantes)}")
        print(f"Cupos disponibles: {self.capacidad - len(self.estudiantes)}")