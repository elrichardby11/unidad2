import sqlite3 as db
from curso.curso import Curso
from persona.conexion import listarPersona

DB_NAME = "academia.db"
PATH = "sqlite/academia.db"

def createTable():
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS CURSO (
                SIGLA VARCHAR(5) PRIMARY KEY,
                NOMBRE VARCHAR(50) NOT NULL,
                DOCENTE VARCHAR(15),
                FOREIGN KEY (DOCENTE) REFERENCES PERSONA(RUT)
            );
""")
    except Exception as e:
        print("Error al crear Base de Datos, Error:", e)

def insertCurso(curso: Curso):
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO CURSO VALUES (?,?, NULL)", 
                           (curso.sigla,
                            curso.nombre,
                           ))
    except Exception as e:
        print("No se ha podido insertar datos a la base de datos, Error:", e)
    else:
        return "Se ha insertado el curso correctamente! "
            
def asignarDocente():
    cursos = listarCurso() # Buscar la existencia de cursos
    
    if len(cursos) < 1:
        return "Sin cursos, debe registrar cursos antes de asignar a un docente. "
    
    docentes = listarPersona(8) # Buscar la existencia de docentes

    if len(docentes) < 1:
        return "Sin docentes, debe registrar docentes antes de continuar. "
    
    for curso in cursos:
        print(curso)

    opcionCurso = input("Ingrese la sigla del curso para asignarla a un docente: ")

    if not (any(curso.sigla == opcionCurso for curso in cursos)): # Buscar si existe "sigla" dentro del resultado de la consulta
        return "No existe la sigla ingresada. "

    for docente in docentes:
        print(docente)

    opcionDocente = input(f'Ingrese el RUT del docente para el curso "{opcionCurso}": ')

    if not (any(docente.rut == opcionDocente for docente in docentes)): # Buscar si existe "RUT" del docente dentro del resultado de la consulta
        return "El rut ingresado no coincide con ningun docente"

    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE CURSO SET (DOCENTE) = (?) WHERE SIGLA = (?);", 
                           (opcionDocente,
                            opcionCurso,
                           ))
    except Exception as e:
        print("No se ha podido asignar docente, Error:", e)
    
    else:
        return "Se ha asignado el docente correctamente! "
        
def listarCurso():
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CURSO;")

    except Exception as e:
        print("No se ha podido mostrar los cursos, Error:", e)

    else:
        listCursos = list()
        for fila in cursor:
            curso = Curso(fila[0], fila[1])
            listCursos.append(curso)
        return listCursos
        