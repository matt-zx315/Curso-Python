"""
Métodos

São funções que representam os comportamentos dos objetos, ou seja,
as ações uqe esse objeto pode realizar no seu sistema. Ex.: uma lâmpada
que pode acender ou apagar.

OBS.: O método __init__ é um métdod especial chamado de construtor. Sua função
é construir o objeto a partir da classe.

Métodos iniciados e terminados em dunder (Double UNDERline) são chamados, em Python, de métodos mágicos.

EVITAR a criação de métodos dunder para não haver risco de conflitar com funções internas do Python,
comprometendo o funcionamento do sistema desenvolvido.

Nomes de métodos são escritos com iniciais minúsculas e sopearados por underline quando
são compostos por mais de uma palavra.

São divididos em 2 grupos:
    - métodos de instância
    - métodos de classe

 Métodos de instância:
    - precisam de uma instância da classe (objeto) para serem executados.
    - modificam atributos apenas da instância que os chama.

 Métodos de classe:
    - não fazem acesso a atributos de instância
    - são conhecidos como "métodos estáticos" em outras linguagens.
    - dão acesso à classe e aos atributos de classe

Métodos também podem ser privados. São sempre iniciados com duplo underline (__).
Também podem ser acessados utilizando Name Mangling.

A linguagem Python possui, ainda, os métodos estáticos, assim como outras linguagens.
Esses métodos não dão acesso nem à classe nem aos atributos de uma instância, mas
podem ser chamados tanto pela classe quanto por uma instância.
"""
from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, _tensao, _cor, _luminosidade):
        self.__tensao = _tensao
        self.__cor = _cor
        self.__luminosidade = _luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, _limite, _saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = _limite
        self.__saldo = _saldo


class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self, _nome, _descricao, _valor):
        self.__nome = _nome
        self.__descricao = _descricao
        self.__valor = (_valor * Produto.imposto * 100) / 100
        self.__id = Produto.contador + 1
        Produto.contador = self.__id

    def desconto(self, _porcentagem):
        """Retorna o valor do produto com desconto."""
        return self.__valor * (100 - _porcentagem) / 100


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):  # cls indica que é um método de classe.
        print(f'Temos {cls.contador} usuários registrados!')

    @staticmethod
    def definicao():
        print("VSF_616")

    def __init__(self, _nome, _sobrenome, _email, _senha):
        self.__id = Usuario.contador + 1
        self.__nome = _nome
        self.__sobrenome = _sobrenome
        self.__email = _email
        # self.__senha = cryp.encrypt(_senha, rounds=200_000, salt_size=16)  # Será descontinuado no passlib 2.0
        self.__senha = cryp.hash(_senha, rounds=200_000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}.')

        """
        rounds -> Número de embaralhamentos que serão realizados
        salt_size -> tamanho do texto que será usado para embaralhar
        """

    def nome_completo(self):  # self indica que é um método de instância.
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, _senha):
        # Verificando se a senha passada bate com a senha armazenada.
        if cryp.verify(_senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


p1 = Produto("Playstation 4", "Eletrônico", 2300)

# Métodos de instância:

print(p1.desconto(20))  # Imprimindo valor com 20% de desconto.
print(Produto.desconto(p1, 20))  # Forma não convencional de chamar um método de instância.

user1 = Usuario("Noé", "Dassua Konta", "fodasse@gmail.com", "607070_e_nao_levanta")
user2 = Usuario("Diva", "Gina", "divag@hotmail.com", "6969-abc")

print(user1.nome_completo())
print(user2.nome_completo())

print(user1._Usuario__senha)  # Senha não criptografada

# nome = input("Informe seu nome: ")
# sobrenome = input("Informe seu sobrenome: ")
# email = input("Informe seu email: ")
# senha = input("Informe sua senha: ")
# confirma_senha = input("Confirme sua senha: ")
#
# if senha == confirma_senha:
#     user3 = Usuario(nome, sobrenome, email, senha)
#     print("Usuário criado com sucesso!")
# else:
#     print("Senha não confere.")
#     exit(1)  # Encerra a execução do programa e imprime o código passado. Geralmente o valor é 1.
#
# senha = input("Informe sua senha: ")
#
# if user3.checa_senha(senha):
#     print(f"Bem vindo de volta, {user3.nome_completo()}!")
# else:
#     print("Senha não confere.")

# Métodos de classe:
Usuario.conta_usuarios()
user1.conta_usuarios()  # Forma incorreta, porém possível de chamar o método de classe.

# Métodos estáticos:
user1.definicao()
Usuario.definicao()
