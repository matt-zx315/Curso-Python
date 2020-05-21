"""
Duck typing

O tipo ou a classe ou objeto é menos importante do que
os métodos que os definem, e ao invés de checar a classe
ou tipo de dado é checada a presença, ou não, de métodos
ou atributos específicos.

Exemplo: o método len() é executado independentemente do
tipo de dado do qual ele faz parte. Contanto que ele seja
definido na classe antes da instânciação, ele poderá ser
chamado a qualquer momento.

O nome 'duck typing' vem da ideia de que 'se isso parece
com um pato, anda como um pato e nada como um pato, então
isso é um pato', ou seja, objetos similares devem ter
atributos e métodos similares.
"""


class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))

nome = 'Nepu'
lista = [12, 34, 56, 78, 90]
dicionario = {"Carlos": 12, "Vanessa": 32, "Joana": 49}

print(len(nome))
print(len(lista))
print(len(dicionario))
