"""
Fazendo uso de annotations.

Annotations, do inglês 'anotações', indicam os tipos de variáveis,
parâmetros, atributos, funções e métodos.

Escrevendo corretamente:

- Variáveis/Parâmetros/Atributos:
    idade: int = 12
    __nome: str = 'Marcos'
    matriculado: bool = True
    media: float

- Funções/Métodos:
    def cumprimentar() -> str:
    def soma(a: float, b: float) -> float:
    def executar(online: bool = True) -> None:
"""
import math


def circunferencia(_raio: float) -> float:
    return 2 * math.pi * _raio


print(circunferencia.__annotations__)  # Imprimindo os type hints da função.

idade: int = 12
__nome: str = 'Marcos'
matriculado: bool = True
media: float  # Não é necessário atribuir um valor ao usar annotations.

print(__annotations__)  # Imprime as anotações das variáveis globais.


class Pessoa:
    def __init__(self, _nome: str, _idade: int, _peso: float) -> None:
        self.__nome: str = _nome
        self.__idade: int = _idade
        self.__peso: float = _peso

    def andar(self, _nome) -> str:
        return f'{self.__nome} está andando'


pessoa = Pessoa("Ana", 12, 46.5)

print(pessoa.__dict__)  # Type hinting em orientação a objetos. Instâncias não possuem annotations.
print(pessoa.andar.__annotations__)  # É necessário acessar os annotations das funções.
print(pessoa.__init__.__annotations__)  # Só é possível ver os annotations dos parâmetros e do retorno.
