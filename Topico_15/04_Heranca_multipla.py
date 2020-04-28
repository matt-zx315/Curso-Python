"""
Herança múltipla

É a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a herdeira possua todos os atributos e métodos
das classes herdadas.

Pode ser feita de duas maneiras:

    - Multiderivação direta
    - Multiderivação indireta

OBS.: Independentemente do tipo de herança, a subclasse herdará
TODOS os métodos e atributos das superclasses.
"""
# Multiderivação direta
class Base1:
    pass
class Base2:
    pass
class Base3:
    pass
class HerdeiraA(Base1, Base2, Base3):  # Herdando diretamente das 3 classes
    pass

# Multiderivação indireta
class Base4:
    pass
class Base5(Base4):
    pass
class Base6(Base5):
    pass
class HerdeiraB(Base6):  # Herdando de uma classe, que herda de outra e assim por diante, ou seja, indiretamente.
    pass


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


pinguim = Pinguim("Pingu")
baleia = Aquatico("Wally")
tatu = Terrestre("Bola")

print(baleia.nadar())
print(baleia.cumprimentar())
print(tatu.andar())
print(tatu.cumprimentar())
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimentar())  # MRO - Method Resolution Order: interfere a ordem na qual os métodos serão chamados.

# Verificando se o objeto é instância de uma classe:
print(f"pinguim é instância de Pinguim? {isinstance(pinguim, Pinguim)}")
print(f"pinguim é instância de Aquatico? {isinstance(pinguim, Aquatico)}")
print(f"pinguim é instância de Terrestre? {isinstance(pinguim, Terrestre)}")
print(f"pinguim é instância de Animal? {isinstance(pinguim, Animal)}")
print(f"pinguim é instância de object? {isinstance(pinguim, object)}")  # Por padrão, toda classe herda de object.
