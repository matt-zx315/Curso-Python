"""
Atributos representam as características do objeto. Por ele é possível representar
computacionalmente os estados de um objeto.

Os atributos, em Python, são divididos em 3 tipos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos.

 Por convenção, em Python ficou estabelecido que todo atributo de uma classe é público.
 Isso significa que os atributos de uma classe podem ser acessado de qualquer lugar
 do código. Para indicar que o atributo é privado, utiliza-se dunder (double underscore,
 ou __). Essa prática também é conhecida como Name Mangling.

 Atributos de instância:
     - atributos que farão parte de todas as instâncias (objetos)  de uma classe.
     - são alocados na memória a cada novo objeto.
     - São atributos declarados dentro do método construtor.
     OBS.: Método construtor é um método especial utilizado para a criação do objeto.
     Esses atributos podem ser púbicos ou privados, ou seja, se eles podem ser acessados
     de fora da classe ou apenas internamente.

 Atributos de classe:
    - atributos declarados diretamente na classe, fora do construtor.
    - geralmente já são inicialmente com um valor.
    - todas as instâncias da classe terão esse mesmo valor.
    - são alocados somente uma vez na memória

 Atributos dinâmicos:
    - atributos de instância criados em tempo de execução
    OBS.: Será exclusivo da instância que o criou
    - podem ser apagados em tempo de execução

"""
from math import ceil, floor  # Módulos para arredondamento de valores para cima e para baixo, respectivamente.


class Lampada:
    # OBS.: a palavra self indica o objeto que está executando o método e/ou contém o atributo.
    def __init__(self, _tensao, _cor):
        self.tensao = _tensao  # Atributo de instância: precedido da palavra self.
        self.cor = _cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, _numero, _limite, _saldo):
        self.numero = _numero
        self.limite = _limite
        self.saldo = _saldo


class Produto:
    def __init__(self, _nome, _descricao, _valor):
        self.nome = _nome
        self.descricao = _descricao
        self.valor = _valor


class Usuario:
    def __init__(self, _nome, _email, _senha):
        self.nome = _nome
        self.email = _email
        self.senha = _senha


class Teste:
    # Não é obrigatório o uso da palavra self, mas não é convencional o seu desuso.
    def __init__(cerveja, nome, idade):
        cerveja.nome = nome
        cerveja.idade = idade


# Classes com atributos privados:


class Acesso:
    def __init__(self, _email, _senha):
        self.email = _email
        self.__senha = _senha


user = Acesso("fulano@gmail.com", 123456)

print(user.email)
# print(user.__senha)  # AttributeError
print(dir(user))  # Imprime, entre os atributos e métodos, o atributo _Acesso__senha
print(user._Acesso__senha)  # Name Mangling = junta underline, nome da classe e nome do atributo privado.

# Atributos de instância:
p1 = Produto("Playstation 4", "Video game", 2300)
p2 = Produto("XBox One S", "Video game", 2100)

print(p1.valor)  # Acesso a um atributo de instância: nome_da_instância.atributo_de_instância
print(p2.valor)

# Atributos de classe:


class Produto:
    imposto = 1.05  # acrésimo de 5% no valor do produto de imposto.
    contador = 0

    def __init__(self, _nome, _descricao, _valor):
        self.nome = _nome
        self.descricao = _descricao
        self.valor = floor(_valor * Produto.imposto * 100) / 100  # O valor de imposto será sempre o mesmo
        self.id = Produto.contador + 1
        Produto.contador = self.id


p1 = Produto("Playstation 4", "Video game", 2300)
p2 = Produto("XBox One S", "Video game", 2100)

print(p1.valor)
print(p2.valor)
print(Produto.imposto)  # Acessando um atributo de classe: nome_da_classe.atributo_de_classe
print(p1.id)
print(p2.id)
print(Produto.contador)

# OBS.: É possível acessar o atributo de classe por meio de uma instância, mas não é uma prática convencional.
print(p1.contador)

# Atributos dinâmicos:
p3 = Produto("Arroz", "Mercearia", 6.00)
p3.peso = "5 kg"

print(p3.peso)  # peso é um atributo exclusivo da instância p3 de produto.

print(p1.__dict__)  # Propriedades de um objeto
print(p2.__dict__)
print(p3.__dict__)
print(Produto.__dict__)

# Apagando atributos:

del p3.peso

print(p3.__dict__)
