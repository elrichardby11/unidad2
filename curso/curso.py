class Curso():
    def __init__(self, sigla: str, nombre: str) -> None:
        self.__sigla = sigla
        self.__nombre = nombre

    @property
    def sigla(self):
        return self.__sigla
    
    @sigla.setter
    def sigla(self, sigla):
        self.__sigla = sigla
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self) -> str:
        return f"""
            Sigla: {self.__sigla}
            Nombre: {self.__nombre}
        """
