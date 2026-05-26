class Estudiante:
    contador_id = 1

    def __init__(self, nombre, apellido, matricula, carrera):
        self.id_estudiante = Estudiante.contador_id
        Estudiante.contador_id += 1
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos = []

    def inscribir_curso(self, curso):
        self.cursos.append(curso)

    def baja_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)

    def mostrar_datos(self):
        print(f"\nID: {self.id_estudiante}")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        if self.cursos:
            print("Cursos inscriptos:")
            for curso in self.cursos:
                print(f"- {curso.nombre}")
        else:
            print("No está inscripto en cursos")
