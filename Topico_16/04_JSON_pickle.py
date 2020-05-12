"""
JSON e Pickle

JSON -> JavaScript Object Notation

API - Meio de comunicação entre serviços fornecidos por empresas
(Twitter, Facebook, YouTube etc.) e terceiros (desenvolvedores).
Geralmente essas APIs estão em formato .json
"""
import json

ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', 'Bivolt', 2430)}])

print(type(ret))
print(ret)
"""
JSON trabalha apenas com aspas duplas.
Strings Python criadas com aspas simples são formatadas pelo método dumps().
"""
import jsonpickle


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

ret = json.dumps({"Felix": felix.__dict__, "Pluto": pluto.__dict__})
print(ret)

"""
Integrando JSON e Pickle:

pip install jsonpickle
"""
gato_json = jsonpickle.encode(felix)
print(gato_json)  # {"py/object": "__main__.Gato", "nome": "Felix", "som": "miado"} -> Objeto Python convertido em JSON.
cachorro_json = jsonpickle.encode(pluto)
print(cachorro_json)

# # Escrevendo o arquivo json/pickle
# with open("JSON/animais.json", 'w') as animais:
#     dado = jsonpickle.encode(felix)
#     animais.write(dado)

# Lendo o arquivo json/pickle
with open("JSON/animais.json", 'r') as animais:
    conteudo = animais.read()
    ret = jsonpickle.decode(conteudo)

    print(ret.nome)
    print(ret.som)
    ret.faz_som()
