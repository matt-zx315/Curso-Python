"""
Conhecendo Pickle

Realiza a seguinte função:

Objeto Python -> Binarização (Serialização)
Binarização -> Objeto Python (Desserialização)

OBS.: O módulo Pickle não é seguro contra dados maliciosos.
Isso significa que não é recomendável trabalhar com arquivos
pickle de fontes desconhecidas e/ou não confiáveis.
"""
import pickle


class Animal:
    def __init__(self, _nome):
        self.nome = _nome

    def comer(self):
        print(f"{self.nome} está comendo.")


class Gato(Animal):
    def __init__(self, _nome, _som):
        super().__init__(_nome)
        self.som = _som

    def faz_som(self):
        print(f"{self.nome} está fazendo som de {self.som}")


class Cachorro(Animal):
    def __init__(self, _nome, _som):
        super().__init__(_nome)
        self.som = _som

    def faz_som(self):
        print(f"{self.nome} está fazendo som de {self.som}")


felix = Gato("Felix", "miado")
pluto = Cachorro("Pluto", "latido")

# Escrevendo em arquivos .pickle
with open("JSON/animais.pickle", 'wb') as animais:
    pickle.dump((felix, pluto), animais)

# Lendo arquivos .pickle
with open("JSON/animais.pickle", 'rb') as animais:
    gato, cachorro = pickle.load(animais)

    print(f"O cachorro se chama {cachorro.nome} e o gato se chama {gato.nome}.")
    gato.faz_som()
    cachorro.faz_som()

    print(type(gato))
    print(type(cachorro))
