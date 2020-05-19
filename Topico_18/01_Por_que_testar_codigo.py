"""
Por que testar o código?

          Aplicação Web
----------------------------------
|            Front End           |
|            Back End            |
----------------------------------
|      Testes Automatizados      |
----------------------------------

Motivos para testar o códigos:
    - detectar, corrigir e reduzir a incidência de bugs (erros) no software
    - garantir que novos recursos do programa não 'quebrem' recursos antigos

Vertente de testes automatizados TDD: Test-Driven Development (Desenvolvimento Guiado por Código)
Nessa vertente, são utilizados estágios de desenvolvimento:
    - Primeiro o teste é escrito
    - A seguir, deve-se escrever o código necessário para cumprir os requisitos do teste
    - Por fim, refatorar o código para executar a funcionalidade e reliza-se um novo teste
    - Ao passar no teste, o recurso é considerado completo

Os estágios do TDD são conhecidos como:
    - Red (falhou)
    - Green (aprovado)
    - Refactor (reescrever)
"""


class Gato:
    def __init__(self, _nome):
        self.__nome = _nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando.')


gato = Gato("Pudim")

# Teste manual
gato.miar()
print(gato.nome)
