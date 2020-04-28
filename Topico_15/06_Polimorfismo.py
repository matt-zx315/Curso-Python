"""
Polimorfismo

 - Do latim:
    - Poli: muitos, vários
    - Morfos: formas

Ao reimplementar um método da superclasse nas subclasses, o método
é sobrescrito (overriding).

Esse é o melhor exemplo de polimorfismo: métodos que realizam diferentes
operações de acordo com as classes que os herdam.
"""


class Animal:
    def __init__(self, _nome):
        self.__nome = _nome

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        raise NotImplementedError("Necessário implementar o métddo na subclasse.")

    def comer(self):
        print(f"{self.__nome} está comendo.")


class Cachorro(Animal):
    def __init__(self, _nome):
        super().__init__(_nome)

    def falar(self):
        print(f"Humano, {self.nome} quer comida!")


class Gato(Animal):
    def __init__(self, _nome):
        super().__init__(_nome)

    def falar(self):
        print(f"Humano, obedeça as ordens de {self.nome}!")


gato = Gato("Felix")
gato.comer()
gato.falar()

cachorro = Cachorro("Pluto")
cachorro.comer()
cachorro.falar()



