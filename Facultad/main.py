from classFacultad import SistemaFacultad
from menu import mostrar_menu

def main():
    sistema = SistemaFacultad()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.registrar_estudiante()

        elif opcion == "2":
            sistema.registrar_curso()

        elif opcion == "3":
            sistema.inscribir_estudiante()

        elif opcion == "4":
            sistema.baja_curso()

        elif opcion == "5":
            sistema.mostrar_cursos()

        elif opcion == "6":
            sistema.mostrar_estudiantes()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
