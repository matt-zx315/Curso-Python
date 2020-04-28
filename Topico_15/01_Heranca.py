"""
Herança

A ideia de herança é a de reaproveitar código e estender classes.

A partir de uma classe existente, é possível estender uma classe,
permitindo que essa herde os atributos e métodos da classe anterior.

Exemplo: cliente e funcionário de um banco

Cliente:
    - nome
    - sobrenome
    - cpf
    - renda

Funcionário:
    - nome
    - sobrenome
    - cpf
    - matrícula

Ambas as classes têm 3 atributos em comum.

Quando uma classe herda de outra, a classe herdeira passa a ter
todos os atributos e métodos da classe herdada. Esta classe é
conhecida como:
    - superclasse
    - classe mãe
    - classe pai
    - classe base
    - classe genérica

A classe herdeira é conhecida como:
    - subclasse
    - classe filha
    - classe específica


Sobrescrita de método (method override)

Ocorre quando um método de uma superclasse é reescrito/reimplementado nas subclasses.
É utilizado para reescrever métodos para que estes sejam executados da maneira desejada
nas subclasses, caso necessário.

OBS.: É necessário, para acessar atributos privados herdados da superclasse, o uso do
recurso de name mangling ou por meio de um método da própria superclasse. É importante notar
que mesmo a classe herdeira não tem acesso aos atributos privados da classe herdada,
sendo necessário o uso de métodos da superclasse. Dessa forma, métodos get/set deverão
ser reescritos sempre nas subclasses no caso de haver atributos privados das classes
herdeira e herdada sendo acessados.
"""


class Pessoa:
    def __init__(self, _nome, _sobrenome, _cpf):
        self.__nome = _nome
        self.__sobrenome = _sobrenome
        self.__cpf = _cpf

    def dados_pessoa(self):
        return f"{self.__nome} {self.__sobrenome}"

    def get_nome(self):
        return self.__nome


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, _nome, _sobrenome, _cpf, _renda):
        super().__init__(_nome, _sobrenome, _cpf)  # Acesso à superclasse da classe herdeira (forma comum)
        self.__renda = _renda

    def dados_pessoa(self):
        return f"{self._Pessoa__nome} {self._Pessoa__sobrenome}, CPF: {self._Pessoa__cpf}"  # Acesso por name mangling


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, _nome, _sobrenome, _cpf, _matricula):
        Pessoa.__init__(self, _nome, _sobrenome, _cpf)  # Outra forma de acessar o construtor da superclasse (não comum)
        self.__matricula = _matricula

    def dados_pessoa(self):
        return f"{super().dados_pessoa()}, matrícula: {self.__matricula}"  # Acesso por método da superclasse.


cliente = Cliente("Marcos", "Almeida de Souza", "025.693.745-10", 2500.0)
funcionario = Funcionario("Bruno", "Santos Prestes", "687.128.637-26", "160.968.25-3")

print(cliente.__dict__)
print(funcionario.__dict__)

print(cliente.dados_pessoa())
print(funcionario.dados_pessoa())

print(funcionario.get_nome())
