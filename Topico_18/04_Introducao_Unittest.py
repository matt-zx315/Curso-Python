"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

Teste unitário = Forma de testar unidades individuais do código.
Unidades individuais podem ser:
    -funções
    -métodos
    -classes
    -módulos

OBS.: Teste unitário não é específico da linguagem Python,
mas de toda a área de desenvolvimento de software.

Para a criação de testes, são criadas classes que herdam de
unittest.TestCase. A partir daí, a classe ganha acesso a todos
os assertions presentes no módulo, podendo testar todas as
unidades do código.

Para executar os testes, é utilizado unittest.main()

TestCase = Caso de teste
São casos de teste para a unidade.

A lista completa das assertions pode ser encontrada em:
https://docs.python.org/3.6/library/unittest.html?highlight=unittest#unittest.TestCase.debug

Para executar os testes no terminal:
python <nome do módulo>
Modo verbose:
python <nome do módulo> -v

É possível (e recomendado) utilizar doctests nos métodos de teste.
"""
import unittest
from Modulos.Atividades import comer, dormir, eh_engracada


class Atividades(unittest.TestCase):
    # Por convenção, todos os testes devem começar com test_<função>
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('alface', True),
            'Estou comendo alface porque é saudável.'
        )

    # Funções de teste diferentes para cada teste da mesma função para maior precisão nos resultados
    def test_comer_saborosa(self):
        self.assertEqual(
            comer(_comida='pizza', _saudavel=False),  # É possível usar parâmetros nomeados
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado depois de dormir por 4 horas.'
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Dormi demais! 10 horas de sono.'
        )

    def test_engracada(self):
        # self.assertEqual(eh_engracada('Faustão'), True)
        # self.assertFalse(eh_engracada('Datena'), False)  # Funções não implementadas passam nesse teste.
        self.assertFalse(eh_engracada('Silvio Santos'), 'Quem quer dinheiro?')  # Comentários podem ser adicionados.
        self.assertTrue(eh_engracada('Ari Toledo'), 'Como piada suja não tem graça?')


if __name__ == "__main__":
    unittest.main()
