"""
Assertions (Asserções)

Uso da palavra reservada assert para realizar asserções simples nos testes.

Assert é usada em expressões para checar se é válida ou não.
Retorna None se a expressão for verdadeira e levanta um
AssertionError no caso de uma expressão falsa.

OBS.:

1) É possível, ainda, especificar um segundo argumento ou
mensagem de erro personalizada.

2) A palavra assert pode ser utilizada em qualquer parte do código,
e não apenas nos testes.
"""
# num1, num2 = 4, 2
# assert 4 == 4  # Não retorna nada
# # assert 4 == 2  # Levanta um AssertionError
# assert num1 == num2, f'{num1} não é igual a {num2}!'


def soma_positivos(*_numeros):
    _soma = 0
    for _num in _numeros:
        assert _num > 0, f'{_num} é menor ou igual a 0.'
        _soma += _num

    return _soma


print(soma_positivos(9, 5, 4, 6, 3))
# print(soma_positivos(9, 5, -4, 6, 3))  # Uma asserção falsa interrompe toda a execução do código.


def recebe_pedido(*_pedidos):
    _cardapio = ['pizza', 'sorvete', 'torta', 'batata frita', 'cachorro-quente', 'hamburguer']
    for _pedido in _pedidos:
        assert _pedido in _cardapio, f'A comida precisa estar na lista:\n{_cardapio}'

    print(f'{_pedidos} saindo!')


recebe_pedido('pizza', 'sorvete', 'batata frita')
# recebe_pedido('pizza', 'bolo', 'sorvete', 'batata frita')

"""
OBS.: Ao executar o Python pelo console com a flag -O,
mesmo que haja o uso do assert, este será igonorado e
o código  executará novamente, mesmo que um parâmetro
inválido seja passado. Burlar essa verificação pode
causar problemas inesperados no sistema, por exemplo:

def faca_algo_ruim(_usuario):
    assert _usuario.eh_admin, 'Somente usuários podem fazer algo ruim.'
    destruir_o_sistema_inteiro()
    return 'Deu bode!'
"""
