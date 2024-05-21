from persona.conexion import createTable as persona
from curso.conexion import createTable as curso
from matriculas.conexion import createTable as matricula

def createTables():
    
    persona()
    curso()
    matricula()