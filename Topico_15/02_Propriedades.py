"""
Propriedades (Properties)

Em linguagens de programação que suportam a orientação a objetos, ao serem criados atributos privados,
também são criados os métodos 'getters' e 'setters', os quais acessam esses atributos para retornar
e alterar seus valores, respectivamente.

Em Python, no entanto, é possível realizar as mesmas operações com o uso das propriedades.
Com o uso do decorador @property, é possível criar um método do tipo getter que ainda pode
ser usado na criação do método setter.
Na hora de acessar as propriedades, é possível escrever o código como se estivesse acessando
diretamente o atributo.
"""


class Conta:
    contador = 0

    def __init__(self, _titular, _saldo, _limite):
        self.__numero = Conta.contador + 1
        self.__titular = _titular
        self.__saldo = _saldo
        self.__limite = _limite
        Conta.contador += self.__numero

    def extrato(self):
        return f"{self.__titular}, seu saldo é de R$ {self.__saldo}."

    def sacar(self, _valor):
        self.__saldo -= _valor

    def depositar(self, _valor):
        self.__saldo += _valor

    def transferir(self, _valor, _destino):
        self.sacar(_valor)
        _destino.depositar(_valor)

    def get_titular(self):
        return self.__titular

    def set_titular(self, _titular):
        self.__titular = _titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, _saldo):
        self.__saldo = _saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, _limite):
        self.__limite = _limite


conta1 = Conta("Fulano", 600.0, 12_000.0)
conta2 = Conta("Beltrano", 800.0, 16_000.0)

soma = conta1._Conta__saldo + conta2._Conta__saldo  # Jeito errado
print(soma)

# Métodos "getter" servem para "pegar" os dados privados do objeto sem acessá-los diretamente.
soma = conta1.get_saldo() + conta2.get_saldo()
print(soma)

# Métodos "setter" alteram o valor dos atributos.
print(conta1.get_limite())
conta1.set_limite(16_000.0)
print(conta1.get_limite())


class Conta:
    # Refatorando os métodos get/set com as propriedades:
    contador = 0

    def __init__(self, _titular, _saldo, _limite):
        self.__numero = Conta.contador + 1
        self.__titular = _titular
        self.__saldo = _saldo
        self.__limite = _limite
        Conta.contador += self.__numero

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @numero.setter
    def numero(self, _numero):
        self.__numero = _numero

    @titular.setter
    def titular(self, _titular):
        self.__titular = _titular

    @saldo.setter
    def saldo(self, _saldo):
        self.__saldo = _saldo

    @limite.setter
    def limite(self, _limite):
        self.__limite = _limite

    def extrato(self):
        return f"{self.__titular}, seu saldo é de R$ {self.__saldo}."

    def sacar(self, _valor):
        self.__saldo -= _valor

    def depositar(self, _valor):
        self.__saldo += _valor

    def transferir(self, _valor, _destino):
        self.sacar(_valor)
        _destino.depositar(_valor)


conta1 = Conta("Fulano", 600.0, 12_000.0)
conta2 = Conta("Beltrano", 800.0, 16_000.0)

print(conta1.saldo + conta2.saldo)

print(conta1.titular)
conta1.titular = "Ciclano"
print(conta1.titular)
