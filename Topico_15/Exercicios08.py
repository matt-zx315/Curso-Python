"""
Exercício 1: Criar uma classe Pessoa com os atributos
nome, endereço e telefone. Como métodos, deve possuir:
    - imprimir (imprime na tela todos os atributos)

Exercício 2: Adicionar um método construtor para definir
os valores dos atributos no momento da instanciação.
"""
from Topico_15.heranca.Testa_Equipamento import TestaEquipamento
from Topico_15.sobrecarga.Pessoa import TestaPessoa


class Pessoa:
    def __init__(self, _nome, _endereco, _telefone):
        self.__nome = _nome
        self.__endereco = _endereco
        self.__telefone = _telefone

    def imprimir(self):
        _mensagem = f"Nome: {self.__nome}\n" \
                    f"Endereço: {self.__endereco}\n" \
                    f"Telefone: {self.__telefone}"

        print(_mensagem)


"""
Exercício 3: Criar a classe Quadrado com os atributos
lado, área e perímetro, tendo como métodos:
     - calcular área (define o valor de área)
     - calcular perímetro (define o valor de perímetro)

Exercício 4: Implementar um construtor na classe
"""


class Quadrado:
    def __init__(self, _lado):
        self.__lado = _lado
        self.__area = 0
        self.__perimetro = 0

    def calcula_area(self):
        self.__area = self.__lado ** 2

    def calcula_perimetro(self):
        self.__perimetro = self.__lado * 4


"""
Exercício 5: Criar a classe retângulo com os atributos
altura, comprimento, área e perímetro. Os métodos são:
     - calcular área (define o valor de área)
     - calcular perímetro (define o valor de perímetro)

Exercício 6: Criar um método construtor
"""


class Retangulo:
    def __init__(self, _altura, _comprimento=None):
        self.__altura = _altura
        self.__area = 0
        self.__perimetro = 0

        # Um retângulo também pode ser um quadrado. Se os lados forem iguais, não é preciso passar dois argumentos.
        if _comprimento is None:
            self.__comprimento = _altura
        else:
            self.__comprimento = _comprimento

    def calcula_area(self):
        self.__area = self.__altura * self.__comprimento

    def calcula_perimetro(self):
        self.__perimetro = (self.__altura + self.__comprimento) * 2


"""
Exercício 7: Criar uma classe círculo com atributos
raio, área e perímetro. Os métodos são:
    - calcular área (define o valor de área)
    - calcular perímetro (define o valor de perímetro)

Exercício 8: criar um método construtor.
"""


class Circulo:
    def __init__(self, _raio):
        self.__raio = _raio
        self.__area = 0
        self.__perimetro = 0

    def calcula_area(self):
        self.__area = ((3.14 * (self.__raio ** 2)) * 100) / 100

    def calcula_perimetro(self):
        self.__perimetro = ((2 * 3.14 * self.__raio) * 100) / 100


"""
Exercício 9 - 16: Criar uma classe Moto com os atributos
marca, modelo, cor, marcha atual, menor marcha, maior marcha e
ligada. Os métodos são:
    - imprimir (imprime os valores de todos os atributos)
    - marcha acima (aumenta uma marcha caso não esteja na mais alta) 
    - marcha abaixo (diminui uma marcha caso não esteja na mais baixa)
    - ligar (muda o estado da moto para 'ligada') 
    - desligar (muda o estado da moto para 'desligada')

A classe deverá ter um construtor para definir os valores dos atributos
no momento da instanciação. 
"""


class Moto:
    def __init__(self, _marca, _modelo, _cor, _marcha_atual=0, _maior_marcha=6, _ligada=False):
        self.marca = _marca
        self.modelo = _modelo
        self.cor = _cor
        self.marcha_atual = _marcha_atual
        self.maior_marcha = _maior_marcha
        self.ligada = _ligada

    def imprimir(self):
        print(f"Marca: {self.marca}\n"
              f"Modelo: {self.modelo}\n"
              f"Cor: {self.cor}\n"
              f"Marcha atual: {self.marcha_atual}\n"
              f"Maior marcha: {self.maior_marcha}\n"
              f"Está ligada? {self.ligada}")

    def marcha_acima(self):
        if self.marcha_atual < self.maior_marcha:
            self.marcha_atual += 1

    def marcha_abaixo(self):
        if self.marcha_atual > 0:
            self.marcha_atual -= 1

    def ligar(self):
        if not self.ligada:
            self.ligada = True

    def desligar(self):
        if self.ligada:
            self.ligada = False


"""
Exercícios 17 - 19: Criar a classe eletrodoméstico com o atributo
ligado e como métodos:
    - imprimir (retorna os valores dos atributos)
    - ligar (muda o valor de ligado para True)
    - desligar (muda o valor de ligado para False)

Criar um método construtor.
"""


class Eletrodomestico:
    def __init__(self, _ligado):
        self.__ligado = _ligado

    def imprimir(self):
        print(f"Está ligado? f{self.__ligado}")

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True

    def desligar(self):
        if self.__ligado:
            self.__ligado = False


"""
Exercícios 20 - 25: Criar uma classe Televisor com os atributos
volume, canal, volume máximo, número de canais e ligada. Os métodos
são:
    - imprimir (imprime os valores dos atributos)
    - ligar (altera o valor de ligado para True)
    - desligar (altera o valor de ligado para False)
    - aumentar volume (aumenta o valor de volume até o máximo de 1 em 1)
    - diminuir volume (diminui o valor de volume até 0 de 1 em 1)
    - canal acima (aumenta o valor de canal até o número de canais máximo de 1 em 1, voltando pra 1 caso passe)
    - canal abaixo (diminui o valor de canal até 0 de 1 em 1, voltando pro valor máximo caso passe)

Criar um construtor para definir atributos
"""


class Televisor:
    def __init__(self, _max_volume=100, _volume=25, _max_canais=999, _canal=10, _ligado=False):
        self.max_volume = _max_volume
        self.volume = _volume
        self.max_canais = _max_canais
        self.canal = _canal
        self.ligado = _ligado

    def imprimir(self):
        print(f"Está ligada? {self.ligado}\n"
              f"Canal: {self.canal}\n"
              f"Número de canais: {self.max_canais}\n"
              f"Volume: {self.volume}\n"
              f"Volume máximo: {self.max_volume}\n")

    def ligar(self):
        if not self.ligado:
            self.ligado = True

    def desligar(self):
        if self.ligado:
            self.ligado = False

    def canal_acima(self):
        if self.canal < self.max_canais:
            self.canal += 1
        else:
            self.canal = 1

    def canal_abaixo(self):
        if self.canal < 1:
            self.canal -= 1
        else:
            self.canal = self.max_canais

    def aumenta_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1

    def diminui_volume(self):
        if self.volume > 0:
            self.volume -= 1


"""
Exercícios 26 - 31: Criar uma classe microondas com
os atributos ligado e porta fechada. Os métodos são:
    - imprimir (imprime os atributos)
    - ligar (altera o valor de ligado para True)
    - desligar (altera o valor de ligado para False)
    - fechar porta (altera o valor de porta fechada para True)
    - abrir porta (altera o valor de porta fechada para False)

Implementar um método construtor.
"""


class Microondas:
    def __init__(self, _ligado=False, _porta_fechada=True):
        self.__ligado = _ligado
        self.__porta_fechada = _porta_fechada

    def imprimir(self):
        print(f"Está ligado? {self.__ligado}\n"
              f"Porta fechada? {self.__porta_fechada}\n")

    def ligar(self):
        if not self.__ligado and self.__porta_fechada:
            self.__ligado = True
        elif not self.__porta_fechada:
            print("FECHA A PORTA, DESGRAÇA!\n")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False

    def abrir_porta(self):
        if self.__porta_fechada and not self.__ligado:
            self.__porta_fechada = False
        elif self.__ligado:
            print("DESLIGA ANTES, ANIMAL!\n")

    def fechar_porta(self):
        if not self.__porta_fechada:
            self.__porta_fechada = True


"""
Exercício 32 - 39: Criar um pacote de nome heranca
e uma classe de nome equipamento com 2 atributos privados.
Criar uma classe computador que herda de equipamento
com 2 atributos privados.
As classes devem ter os métodos de acesso e modificação.
Criar uma classe testar equipamento com o método main(), o
qual exibe informações dos objetos criados. Esses objetos são
um da classe equipamento e outro da classe computador.
A classe equipamento deve ter um método exibe() para mostrar
seus dados, enquanto a classe computador deve ter o método
exibe() sobrescrito.
"""
TestaEquipamento.main()
print(TestaEquipamento.computador.cpu)

"""
Exercício 40 - 52: Em um pacote de nome sobrecarga, criar uma classe
chamada Pessoa. Essa classe deve ter como atributos de instância código,
nome e idade. Deve ter um método sobrecarregado chamado exibe,
o qual mostra o conteúdo de todos os atributos. Na sobrecarga, esse método
imprimirá o valor de idade somente se receber como argumento o valor inteiro
1, bem como um construtor padrão que exibe a mensagem 'Construtor padrão'.
Sobrecarregar o construtor

A seguir, criar uma classe TestaPessoa que instancia um objeto da classe
pessoa. Inicializar os atributos da instância e chamar o método exibe sem
passar nenhum parâmetro, com o valor inteiro 1 e com um valor diferente de 1.
Criar um segundo objeto do tipo Pessoa e chamar o método exibe desse novo
objeto sem nenhum argumento.
"""
tp = TestaPessoa

tp.fulano.codigo = "00164SCV"
tp.fulano.nome = "Fulano"
tp.fulano.idade = 16

tp.fulano.exibe()
tp.fulano.exibe(1)
tp.fulano.exibe("?")
tp.ciclano.exibe()
