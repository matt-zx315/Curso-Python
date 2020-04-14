"""
Objetos -> Instâncias de classes. Após o mapeamento do objeto para sua representação
computacional (classe), podem ser criados quantos objetos forem necessários dentro do
programa. Objetos/instâncias podem ser considerados variáveis do tipo de suas classes.
"""


class Lampada:
    def __init__(self, _tensao, _cor, _potencia):
        self.__tensao = _tensao
        self.__cor = _cor
        self.__potencia = _potencia
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, _nome, _cpf):
        self.__nome = _nome
        self.__cpf = _cpf

    def mostra_nome(self):
        return self.__nome

    def mostra_cpf(self):
        return self.__cpf


class ContaCorrente:
    contador = 4999

    def __init__(self, _limite, _saldo, _cliente=None):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = _limite
        self.__saldo = _saldo
        self.__cliente = _cliente

    def mostra_cliente(self):
        return f"Nome: {self.__cliente.mostra_nome()}, CPF: {self.__cliente.mostra_cpf()}."


class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self, _nome, _descricao, _valor):
        self.__nome = _nome
        self.__descricao = _descricao
        self.__valor = (_valor * Produto.imposto * 100) / 100
        self.__id = Produto.contador + 1
        Produto.contador = self.__id


class Usuario:
    contador = 0

    def __init__(self, _nome, _sobrenome, _email, _senha):
        self.__id = Usuario.contador + 1
        self.__nome = _nome
        self.__sobrenome = _sobrenome
        self.__email = _email
        self.__senha = _senha
        Usuario.contador = self.__id


# Criando objetos/instâncias (spoilers: isso já foi feito VÁRIAS vezes)
lamp1 = Lampada(110, "Azul", 75)
cc1 = ContaCorrente(5_000, 200_000)
user1 = ('Batero', 'Nakombi', 'bateronakombi@aol.com', 'algumacoisa*123')

print(f"{lamp1.checa_lampada()}")
lamp1.liga_desliga()
print(f"{lamp1.checa_lampada()}")

# Passando valor de variáveis como argumentos no construtor
nome = 'Fulano'
sobrenome = 'de Tal'
email = 'fulano_de_tal@uol.com'
senha = 'Eeuseilaporra%666'

user2 = Usuario(nome, sobrenome, email, senha)
print(user2.__dict__)

# Objetos podem ser passados como argumentos nos construtores:
cliente = Cliente('Paula Tejano', '098.765.432-10')
cc2 = ContaCorrente(10_000, 600_000, cliente)

print(cc1.__dict__)
print(cc2.mostra_cliente())
