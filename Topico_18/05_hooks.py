"""
Unittest - Antes e após hooks

hooks - Execução dos testes.

setup() -> É executado antes de cada método de teste. Util para criação de instâncias de objetos e outros dados.
tearDown() -> É executado ao final de cada método de teste. Útil para excluir dados e arquivos ou fechar conexões.

Forma geral:

class ModuloTest(unittest.TestCase):
    def setUp(self) -> None:
        # Configurações do setUp()

    def teste_1(self):
        # setUp() roda antes do teste
        # tearDown() roda depois do teste

    def teste_2(self):
        # setUp() roda antes do teste
        # tearDown() roda depois do teste

    def tearDown(self) -> None:
        # Configurações do tearDown()
"""
import unittest
from Modulos.Robo import Robo


class RoboTeste(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp() em execução...')
        self.megaman = Robo('Mega Man', _bateria=50)

    def test_carregar(self):
        self.megaman.carregar_bateria()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.diz_nome(), 'EU SOU MEGA MAN.')
        self.assertEqual(self.megaman.bateria, 49, 'Mega Man deveria ter 49% de bateria restando.')

    def tearDown(self) -> None:
        print('tearDown() em execução...')


if __name__ == '__main__':
    unittest.main()
