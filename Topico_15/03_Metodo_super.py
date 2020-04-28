"""
Método super

É um método que se refere à superclasse
"""


class Animal:
    def __init__(self, _nome, _especie, _som):
        self.__nome = _nome
        self.__especie = _especie
        self.__som = _som

    def emite_som(self):
        return self.__som


class Gato(Animal):
    def __init__(self, _nome, _especie, _som, _raca):
        super().__init__(_nome, _especie, _som)
        self.__raca = _raca


gato = Gato("Bugato", "Felino", "MRAU", "Siamês")
print(gato.emite_som())
