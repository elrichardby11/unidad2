from controller.database import createTables
from controller.menu import registerPerson, registerCurso, listPerson, asigTeacher, listCurso, enrollSudent, unenrollStudent, listEnrollments, goodBye

createTables() # This create database if it doesn't exist

ESPACIO = 10

def main():
    while True:
        print("\n")
        print("="*ESPACIO, "Menu Principal", "="*ESPACIO)
        print("""
        1  -  Registrar alumno
        2  -  Registrar docente
        3  -  Registrar curso
        4  -  Asignar docente
        5  -  Matricular alumno
        6  -  Dar de baja alumno
        7  -  Listar alumnos
        8  -  Listar docentes
        9  -  Listar cursos
        10 -  Listar matriculas
        11 -  Salir
        """)

        opcion = input("Ingrese una opcion: ")

        if not (opcion.isnumeric()): # Control to "option" value
            print("Ingrese un valor valido! ")
            return
        
        opcion = int(opcion)
        
        if opcion == 1:
            print(registerPerson(opcion))

        elif opcion == 2:
            registerPerson(opcion)
        
        elif opcion == 3:
            registerCurso()
        
        elif opcion == 4:
            asigTeacher()
        
        elif opcion == 5:
            enrollSudent()
        
        elif opcion == 6 :
            unenrollStudent()

        elif opcion == 7:
            print(listPerson(opcion))
        
        elif opcion == 8:
            print(listPerson(opcion))
        
        elif opcion == 9:
            print(listCurso())
        
        elif opcion == 10:
            print(listEnrollments())

        elif opcion == 11:
            goodBye()
            break

        else:
            print("\nIngrese un número válido! ")
main()