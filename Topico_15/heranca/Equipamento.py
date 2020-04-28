class Equipamento:
    def __init__(self, _tipo, _codigo):
        self.__tipo = _tipo
        self.__codigo = _codigo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def codigo(self):
        return self.__codigo

    @tipo.setter
    def tipo(self, _tipo):
        self.__tipo = _tipo

    @codigo.setter
    def codigo(self, _codigo):
        self.__codigo = _codigo

    def exibe(self):
        print(f"Tipo: {self.__tipo}\n"
              f"Código: {self.__codigo}\n")

