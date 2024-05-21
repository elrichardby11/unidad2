import sqlite3 as db

DB_NAME = "academia.db"
PATH = "sqlite/academia.db"

def createTable():
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS MATRICULAS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                SIGLA VARCHAR(5) NOT NULL,
                RUT VARCHAR(15) NOT NULL,
                FOREIGN KEY (SIGLA) REFERENCES CURSO(SIGLA),
                FOREIGN KEY (RUT) REFERENCES PERSONA(RUT)
            );
""")
    except Exception as e:
        print("Error al crear Base de Datos, Error:", e)

def agregarEstudiante(rut:str):
    lista = checkStudent(rut)
    
    if (len(lista) < 1):
        return "Estudiante no encontrado! "

    cursos = listarMatriculas(1, rut)
    if not cursos:
        return "El alumno se encuentra matriculado/a a todas las asignaturas! "
    for curso in cursos:
        print(curso)
    siglas = input("Ingrese la sigla del curso para la matricula: ")

    if not (any(curso[0] == siglas for curso in cursos)): # Buscar si existe "sigla" dentro del resultado de la consulta
        return "No existe la sigla ingresada. "
    
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO MATRICULAS (ID, SIGLA, RUT) VALUES (NULL, ?, ?);", 
                           (siglas,
                            rut,
                           ))
    except Exception as e:
        print("No se ha podido matricular alumno, Error:", e)
    
    else:
        return "Se ha matriculado el alumno correctamente! "

def eliminarEstudiante(rut):
    lista = checkStudent(rut)
    
    if (len(lista) < 1):
        return "Estudiante no encontrado! "

    opcion = input("Desea dar de baja para todas las asignaturas? (S/N): ")

    if (opcion.isascii):
        opcion = opcion.upper()

    if (opcion == "S"):
        try:
            with db.connect(PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM MATRICULAS WHERE RUT = (?);", (rut,))
        except Exception as e:
            print("No se ha podido dar de baja al alumno, Error:", e)
        
        else:
            return "Se ha dado de baja al alumno correctamente! "

    else:            
        cursos = listarMatriculas(2, rut)
        if not cursos:
            return "No se encontraron matriculas para dar de baja! "
        for curso in cursos:
            print(curso)
        
        siglas = input("Ingrese la sigla del curso para dar de baja: ")

        if not (any(curso[0] == siglas for curso in cursos)): # Buscar si existe "sigla" dentro del resultado de la consulta
            return "No existe la sigla ingresada. "
        
        try:
            with db.connect(PATH) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM MATRICULAS WHERE RUT = (?) AND SIGLA = (?);", 
                            (rut,
                            siglas,
                            ))
        except Exception as e:
            print("No se ha podido dar de baja al alumno, Error:", e)
        
        else:
            return "Se ha dado de baja el alumno a la asignatura correctamente! "

def checkStudent(rut):
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PERSONA WHERE RUT = (?) AND TIPO = 'estudiante';", ((rut),))

    except Exception as e:
        print("No se ha podido consultar el estado del estudiante, Error:", e)
    else:
        listStudent = list()
        for student in cursor:
            listStudent.append(student)
        return listStudent
    
def listarMatriculas(option:int, rut=str):
    query = ""
    params = False

    if option == 1: # 1 For the funcion "agregarEstudiante"  
        query = """ SELECT c.SIGLA
                    FROM CURSO c 
                    LEFT JOIN MATRICULAS m
                    ON c.SIGLA = m.SIGLA
                    AND m.RUT = (?) 
                    WHERE m.SIGLA IS NULL;"""
        params = True
    elif option == 2: # 2 For the funcion "eliminarEstudiante"  
        query = "SELECT SIGLA, RUT FROM MATRICULAS WHERE RUT = (?);"
        params = True
    elif option == 10: # For 10 option menu
        query = "SELECT SIGLA, RUT FROM MATRICULAS"
    else:
        return "Error al obtener el valor de 'value'"
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, ((rut,)))
            else:
                cursor.execute(query)

    except Exception as e:
        print("No se ha podido mostrar las matriculas, Error:", e)

    else:
        listEnrollments = list()
        for enrollment in cursor:
            listEnrollments.append(enrollment)
        return listEnrollments
