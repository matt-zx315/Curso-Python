"""
MRO - Method Resolution Order (Ordem de Resolução de Métodos)

É a ordem de execução dos métodos.
Há 3 formas de conferir a MRO:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help()
"""


class Animal:
    def __init__(self, _nome):
        self.__nome = _nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}!"


class Aquatico(Animal):
    def __init__(self, _nome):
        super().__init__(_nome)

    def nadar(self):
        return f"{self.nome} está nadando."

    def cumprimentar(self):
        return f"{super().cumprimentar()} Sou um animal aquático."


class Terrestre(Animal):
    def __init__(self, _nome):
        super().__init__(_nome)

    def andar(self):
        return f"{self.nome} está andando."

    def cumprimentar(self):
        return f"{super().cumprimentar()} Sou um animal terrestre."


class Pinguim(Aquatico, Terrestre):
    def __init__(self, _nome):
        super().__init__(_nome)


pinguim = Pinguim("Tux")
print(pinguim.cumprimentar())

print(Pinguim.__mro__)  # Retorna uma tupla com as classes herdadas
print(Pinguim.mro())  # Retorna uma lista com as classes herdadas
print(help(Pinguim))  # Retorna uma string
