import sqlite3 as db
from persona.persona import Persona

DB_NAME = "academia.db"
PATH = "sqlite/academia.db"

def createTable():
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS PERSONA (
                RUT VARCHAR(15) PRIMARY KEY,
                NOMBRE VARCHAR(12) NOT NULL,
                APELLIDO VARCHAR(50) NOT NULL,
                FECHA_NACIMIENTO DATE NOT NULL,
                TIPO VARCHAR(50) NOT NULL
            );
            """)
    except Exception as e:
        print("Error al crear Base de Datos, Error:", e)

def insertPerson(persona: Persona):
    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PERSONA VALUES (?,?,?,?,?)", 
                           (persona.rut,
                            persona.nombre,
                            persona.apellido,
                            persona.fecha,
                            persona.tipo))

    except Exception as e:
        print("No se ha podido insertar datos a la base de datos, Error:", e)

    else:
        return "\nRegistro ingresado correctamente! "
    
def listarPersona(tipo: int):
    valorTipo = ""
    if tipo == 7:
        valorTipo = "estudiante"
    elif tipo == 8:
        valorTipo = "docente"
    else:
        return "Tipo no valido! " # Return an appropiate message for invalid types

    try:
        with db.connect(PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PERSONA WHERE TIPO = (?);", (valorTipo,))

    except Exception as e:
        print("No se ha podido listar, Error:", e)
    else:

        listPerson = list()
        for person in cursor:
            persona = Persona(person[0], person[1], person[2], person[3], person[4])
            listPerson.append(persona)
        return listPerson