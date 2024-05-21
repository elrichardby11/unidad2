from curso.conexion import insertCurso, asignarDocente, listarCurso
from persona.conexion import insertPerson, listarPersona
from matriculas.conexion import agregarEstudiante, eliminarEstudiante, listarMatriculas

from curso.curso import Curso
from persona.persona import Persona

import time  

TIME = 1.5 # Time for the user to read the output

def registerPerson(tipo: int): # For the option 1 and 2
    valorTipo = ""
    if tipo == 1:
        valorTipo = "estudiante"
    elif tipo == 2:
        valorTipo = "docente"
    else: 
        return "Error al encontrar el valor 'Tipo'"

    rut = input(f"Ingrese el RUT del {valorTipo}: ")
    nombre = input(f"Ingrese el nombre del {valorTipo}: ")
    apellido = input(f"Ingrese el apellido del {valorTipo}: ")
    fecha = input(f"Ingrese la fecha de nacimiento del {valorTipo} (DD-MM-YY): ")
    
    if (not rut) or (not nombre) or (not apellido) or (not fecha):
        return "No ingrese valores vacios/inválidos! "

    persona = Persona(rut, nombre, apellido, fecha, valorTipo)
    print(insertPerson(persona))
    time.sleep(TIME)
    return

def registerCurso(): # For the option 3
    siglas = input("Ingrese las siglas del curso: ")
    nombre = input("Ingrese el nombre del curso: ")
    curso = Curso(siglas, nombre)
    print(insertCurso(curso))
    time.sleep(TIME)
    return

def asigTeacher(): # For the option 4
    print(asignarDocente())
    time.sleep(TIME)
    return

def enrollSudent(): # For the option 5
    rut = input("Ingrese el RUT del estudiante a matricular: ")
    print(agregarEstudiante(rut))
    time.sleep(TIME)
    return

def unenrollStudent(): # For the option 6
    rut = input("Ingrese el RUT del estudiante a dar de baja: ")
    print(eliminarEstudiante(rut))
    time.sleep(TIME)
    return

def listPerson(option: int): # For the option 7 y 8
    personas = listarPersona(option)
    if not personas:
        return "No se encontraron resultados! "
    for persona in personas:
        print(persona)
    time.sleep(TIME)
    return ""

def listCurso(): # For the option 9
    cursos = listarCurso()
    if not cursos:
        return "No hay cursos! "
    for curso in cursos:
        print(curso)
    time.sleep(TIME)
    return ""

def listEnrollments(): # For the option 10
    enrollments = listarMatriculas(10)
    if not enrollments:
        return "No hay matriculas! "
    for enrollment in enrollments:
        print(enrollment)
    time.sleep(TIME)
    return ""

def goodBye(): # For the option 11
    print("Hasta Luego! :=) ")
    time.sleep(TIME)
    return
