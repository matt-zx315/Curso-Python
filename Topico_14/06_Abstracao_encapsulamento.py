"""
Encapsulamento -> agrupamento de atributos e métodos dentro de uma classe.

Abstração -> exposição apenas de dados relevantes de uma classe, escondendo
dados e métodos privados de usuários.
"""


class Conta:
    contador = 400

    def __init__(self, _titular, _saldo, _limite):
        self.numero = Conta.contador
        self.titular = _titular
        self.saldo = _saldo
        self.limite = _limite
        Conta.contador += 1

    def extrato(self):
        print(f"{self.titular}, você tem R$ {self.saldo} de saldo, com limite de R$ {self.limite}.")

    def depositar(self, _valor):
        self.saldo += _valor

    def sacar(self, _valor):
        self.saldo -= _valor


# Deixando os atributos públicos:
conta1 = Conta("Fulano", 50_000, 1_000_000)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# Atributos públicos podem ser alterados diretamente:
conta1.numero = 42
conta1.titular = 'Ciclano'
conta1.saldo = 10
conta1.limite = 1000

print(conta1.__dict__)


# Deixando os atributos privados:
class Conta:
    contador = 400

    def __init__(self, _titular, _saldo, _limite):
        self.__numero = Conta.contador
        self.__titular = _titular
        self.__saldo = _saldo
        self.__limite = _limite
        Conta.contador += 1

    def extrato(self):
        print(f"{self.__titular}, você tem R$ {self.__saldo} de saldo, com limite de R$ {self.__limite}.")

    def depositar(self, _valor):
        self.__saldo += _valor

    def sacar(self, _valor):
        self.__saldo -= _valor


conta2 = Conta('Beltrano', 9_000, 9_000_000)
print(conta2. __dict__)

# Para acessar e alterar os valores do objeto, precisamos de métodos para tal.
conta2.depositar(200)
conta2.extrato()
