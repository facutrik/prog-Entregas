from classEstudiante import Estudiante
from classCurso import Curso
from validaciones import validar_texto, validar_numero


class SistemaFacultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []


    def buscar_estudiante(self, matricula):
        for e in self.estudiantes:
            if e.matricula == matricula:
                return e
        return None


    def buscar_curso(self, codigo):
        for c in self.cursos:
            if c.codigo == codigo:
                return c
        return None


    def registrar_estudiante(self):
        print("\n  Registrar estudiante")
        while True:
            try:
                nombre = validar_texto(input("Nombre: "), "nombre"
                )
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                apellido = validar_texto(input("Apellido: "), "apellido"
                )
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                matricula = validar_numero(input("Matrícula: "),"matrícula")
                estudiante = self.buscar_estudiante(matricula)
                if estudiante is not None:
                    print("Error: La matrícula ya existe")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            carrera = input("Carrera: ").strip()
            if carrera == "":
                print("Error: El campo carrera no puede estar vacío")
            else:
                break
        estudiante = Estudiante(nombre, apellido, matricula, carrera)
        self.estudiantes.append(estudiante)
        print("\nEstudiante registrado correctamente")


    def registrar_curso(self):
        print("\n  Registrar curso")
        while True:
            try:
                nombre = validar_texto(input("Nombre del curso: "), "nombre del curso")
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                codigo = validar_numero(input("Código del curso: "), "código")
                curso = self.buscar_curso(codigo)
                if curso is not None:
                    print("Error: El código ya existe")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                profesor = validar_texto(input("Profesor encargado: "), "profesor")
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                capacidad = validar_numero(input("Capacidad máxima: "), "capacidad")
                capacidad = int(capacidad)
                if capacidad <= 0:
                    print("Error: La capacidad debe ser mayor a 0")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        curso = Curso(nombre, codigo, profesor, capacidad)
        self.cursos.append(curso)
        print("\nCurso registrado correctamente")


    def inscribir_estudiante(self):
        print("\n  Inscribir a curso")
        while True:
            try:
                matricula = validar_numero(input("Ingrese matrícula del estudiante: "), "matrícula")
                estudiante = self.buscar_estudiante(matricula)
                if estudiante is None:
                    print("Error: Estudiante no encontrado")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                codigo = validar_numero(input("Ingrese código del curso: "), "código")
                curso = self.buscar_curso(codigo)
                if curso is None:
                    print("Error: Curso no encontrado")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        if estudiante in curso.estudiantes:
            print("El estudiante ya está inscripto")
            return
        if not curso.hay_cupo():
            print("No hay cupos disponibles")
            return
        curso.agregar_estudiante(estudiante)
        estudiante.inscribir_curso(curso)
        print("\nInscripción realizada correctamente")


    def baja_curso(self):
        print("\n  Bajar de curso")
        while True:
            try:
                matricula = validar_numero(input("Ingrese matrícula del estudiante: "), "matrícula")
                estudiante = self.buscar_estudiante(matricula)
                if estudiante is None:
                    print("Error: Estudiante no encontrado")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        while True:
            try:
                codigo = validar_numero( input("Ingrese código del curso: "), "código")
                curso = self.buscar_curso(codigo)
                if curso is None:
                    print("Error: Curso no encontrado")
                    continue
                break
            except ValueError as e:
                print("Error:", e)
        if estudiante not in curso.estudiantes:
            print("El estudiante no está inscripto en este curso")
            return
        curso.eliminar_estudiante(estudiante)
        estudiante.baja_curso(curso)
        print("\nBaja realizada correctamente")


    def mostrar_cursos(self):
        print("\n  Lista de cursos")
        if len(self.cursos) == 0:
            print("No hay cursos registrados")
            return
        for curso in self.cursos:
            curso.mostrar_estado()


    def mostrar_estudiantes(self):
        print("\n  Lista de estudiantes")
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados")
            return
        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()
