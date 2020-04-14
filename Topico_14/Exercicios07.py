# """
# Exercício 1: Criar uma classe pessoa com os atributos privados
# nome, idade e altura. Criar os métodos para retornar e alterar
# os valores desses atributos e um método para imprimí-los.
# """
#
#
# class Pessoa:
#     def __init__(self, _nome, _idade, _altura):
#         self.__nome = _nome
#         self.__idade = _idade
#         self.__altura = _altura
#
#     def get_nome(self):
#         return self.__nome
#
#     def get_idade(self):
#         return self.__idade
#
#     def get_altura(self):
#         return self.__altura
#
#     def set_nome(self, _nome):
#         self.__nome = _nome
#
#     def set_idade(self, _idade):
#         self.__idade = _idade
#
#     def set_altura(self, _altura):
#         self.__altura = _altura
#
#     def imprime_pessoa(self):
#         print(f"Nome: {self.__nome}\nIdade: {self.__idade} anos\nAltura: {self.__altura} m")
#
#
# pessoa1 = Pessoa("Fulano", 15, 1.68)
#
# pessoa1.imprime_pessoa()
#
# """
# Exercício 2: Criar uma classe agenda que possa armazenar 10 pessoas e possa realizar as operações:
#
#  - armazenar pessoa com os atributos de nome, idade e altura;
#  - remover pessoa pelo nome;
#  - buscar uma pessoa pelo nome e retornar sua posição na agenda;
#  - imprimir todos os registros na agenda;
#  - imprimir o registro apenas de uma pessoa de acordo com a posição passada.
# """
#
#
# class Agenda:
#     def __init__(self):
#         self.pessoas = []
#
#     def armazena_pessoa(self, *args):
#         for _pessoa in args:
#             self.pessoas.append(_pessoa)
#
#     def remove_pessoa(self, _nome):
#         _pessoa = None
#
#         for pessoa in self.pessoas:
#             if pessoa.get_nome() == _nome:
#                 _pessoa = pessoa
#                 self.pessoas.remove(_pessoa)
#             else:
#                 return f"{_nome} não encontrado."
#
#     def encontra_posicao(self, _nome):
#         _posicao = None
#
#         for pessoa in self.pessoas:
#             print(pessoa.get_nome())
#             if pessoa.get_nome() == _nome:
#                 _posicao = self.pessoas.index(pessoa)
#                 return f"{_nome} está na posição {_posicao}."
#         return f"{_nome} não encontrado."
#
#     def imprime_lista(self):
#         for pessoa in self.pessoas:
#             pessoa.imprime_pessoa()
#
#     def imprime_pessoa(self, _posicao):
#         if 0 < _posicao < len(self.pessoas):
#             self.pessoas[_posicao].imprime_pessoa()
#         else:
#             print("Posição inexistente.")
#
#
# pessoa2 = Pessoa("Takaro Nomuro", 19, 1.75)
#
# agenda = Agenda()
#
# agenda.armazena_pessoa(pessoa1, pessoa2)
# agenda.imprime_lista()
#
# print(agenda.encontra_posicao("Takaro Nomuro"))
# print(agenda.encontra_posicao("Diva Gina"))
#
# agenda.imprime_pessoa(1)
# agenda.imprime_pessoa(6)
#
# agenda.remove_pessoa("Fulano")
# agenda.imprime_lista()
#
# """
# Exercício 3: Criar uma classe que representa um elevador em um prédio com os atributos:
# andar atual (padrão = 0), total de andares do prédio (exceto o térreo), andares no subsolo
# (se houver essa opção) capacidade do elevador, número de pessoas dentro. Todos os atributos devem estar encapsulados.
# Deve ter, ainda, os seguintes métodos
#
#  - Inicializar (construtor, começando vazio e no térreo)
#  - Entrar (adiciona pessoas no elevador, desde que não passe da capacidade)
#  - Sair (remove pessoas do elevador, desde que ainda haja pessoas no elevador)
#  - Subir (apenas um andar por vez e caso ainda não esteja no último andar)
#  - Descer (apenas um andar por vez e caso ainda não esteja no último subsolo)
# """
#
#
# class Elevador:
#     def __init__(self, _atual=0, _andares=15, _subsolo=-2, _pessoas=0, _capacidade=10):
#         self.__atual = _atual
#         self.__andares = _andares
#         self.__subsolo = _subsolo
#         self.__capacidade = _capacidade
#         self.__pessoas = _pessoas
#
#     def get_atual(self):
#         return self.__atual
#
#     def get_andares(self):
#         return self.__andares
#
#     def get_subsolo(self):
#         return self.__subsolo
#
#     def get_pessoas(self):
#         return self.__pessoas
#
#     def get_capacidade(self):
#         return self.__capacidade
#
#     def entrar(self, _pessoas):
#         if self.__pessoas + _pessoas <= self.__capacidade:
#             self.__pessoas += _pessoas
#         elif self.__pessoas == self.__capacidade:
#             print(f"Não é possível o embarque no momento.")
#         else:
#             print(f"Só é possível embarcar mais {self.__capacidade - self.__pessoas} pessoas.")
#
#     def sair(self, _pessoas):
#         if self.__pessoas - _pessoas >= 0:
#             self.__pessoas -= _pessoas
#         elif self.__pessoas == 0:
#             print(f"Elevador vazio")
#         else:
#             print(f"Há apenas {self.__pessoas} pessoas no elevador.")
#
#     def subir(self):
#         if self.__atual < self.__andares:
#             self.__atual += 1
#         else:
#             print("Último andar!")
#
#     def descer(self):
#         if self.__atual > self.__subsolo:
#             self.__atual -= 1
#         else:
#             print("Último subsolo!")
#
#
# elevador = Elevador()
#
# elevador.entrar(6)
# elevador.entrar(2)
#
# print(elevador.get_pessoas())
#
"""
Exercício 4: Criar as classes Televisão, com canais e volume, e a classe Controle remoto,
que pode trocar os canais e aumentar o volume da televisão.

 - O volume deve aumentar ou diminuir de uma em uma unidade;
 - Mudar um canal para 'cima' ou para 'baixo' por vez ou trocar diretamente para o canal desejado;
 - Deve ser possível consultar o canal e o volume.
"""


class Televisão:
    def __init__(self, _max_volume=100, _volume=25, _max_canais=999, _canal=10):
        self.max_volume = _max_volume
        self.volume = _volume
        self.max_canais = _max_canais
        self.canal = _canal
        self.ligada = False


class ControleRemoto:
    def __init__(self, _tv):
        self.__tv = _tv

    def aumenta_volume(self):
        if self.__tv.volume < self.__tv.max_volume:
            self.__tv.volume += 1

        print(self.__tv.volume)

    def diminui_volume(self):
        if self.__tv.volume > 0:
            self.__tv.volume -= 1

        print(self.__tv.volume)

    def mostra_volume(self):
        return self.__tv.volume

    def sobe_canal(self):
        if self.__tv.canal < self.__tv.max_canais:
            self.__tv.canal += 1
        else:
            self.__tv.canal = 1

        print(self.__tv.canal)

    def desce_canal(self):
        if self.__tv.canal > 1:
            self.__tv.canal -= 1
        else:
            self.__tv.canal = 999

        print(self.__tv.canal)

    def muda_canal(self, _canal):
        if 1 < _canal < 999:
            self.__tv.canal = _canal

        print(_canal)

    def mostra_canal(self):
        return self.__tv.canal


tv = Televisão()
cr = ControleRemoto(tv)

print(cr.mostra_canal())
print(cr.mostra_volume())

cr.muda_canal(624)
cr.sobe_canal()
cr.desce_canal()
cr.diminui_volume()
cr.aumenta_volume()
