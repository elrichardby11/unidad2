class Persona():
    def __init__(self, rut: str, nombre: str, apellido: str, fechaNacimiento: str, tipo:str) -> None:
        self.__rut = rut
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        self.__tipo = tipo

    @property
    def rut(self):
        return self.__rut
    
    @rut.setter
    def rut(self, rut):
        self.__rut = rut

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def fecha(self):
        return self.__fechaNacimiento
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fechaNacimiento = fecha

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self) -> str:
        return f"""
        Rut: {self.__rut}
        Nombre: {self.__nombre}
        Apellido: {self.__apellido}
        Fecha Nacimiento: {self.__fechaNacimiento}
        Tipo: {self.__tipo}
        """
