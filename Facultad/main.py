
from classFacultad import SistemaFacultad
from menu import mostrar_menu


def main():

    sistema = SistemaFacultad()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                sistema.registrar_estudiante()

            case "2":
                sistema.registrar_curso()

            case "3":
                sistema.inscribir_estudiante()

            case "4":
                sistema.baja_curso()

            case "5":
                sistema.mostrar_cursos()

            case "6":
                sistema.mostrar_estudiantes()

            case "7":
                print("Saliendo del sistema...")
                break

            case _:
                print("Opción inválida")


main()