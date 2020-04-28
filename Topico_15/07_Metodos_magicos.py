"""
Métodos mágicos

São todos os métodos que utilizam dunder(__metodo__)

Dunder init -> __init__  (Método construtor)
Dunder mro -> __mro__    (Apresenra a ordem de execução dos métodos)
Dunder dict -> __dict__  (Retorna os nomes e os valores dos atributos de uma instância em forma de um dicionário)
Dunder repr -> __repr__  (Representa o objeto. Voltado para o desenvolvedor)
Dunder str -> __str__    (Representa o objeto. Voltado para os usuários finais. Tem preferência sobre o __repr__)
Dunder len -> __len__    ('Tamanho' do objeto)
Dunder del -> __del__    (Apaga um objeto da memória)
Dunder add -> __add__    (Concatenação de objetos. Deve ser feito em pares)
Dunder mul -> __mul__    (Multiplicação de valores)
"""


class Livro:
    def __init__(self, _titulo, _autor, _paginas):
        self.titulo = _titulo
        self.autor = _autor
        self.paginas = _paginas

    def __repr__(self):  # Função que retorna um valor que representa a função (sobrescrevendo método de object).
        return self.titulo

    def __str__(self):  # Tem preferência sobre o método __repr__
        return f"{self.titulo}, escrito por {self.autor}."

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f"Objeto {self.titulo} removido")

    def __add__(self, other):
        return f"Livro 1: {self}\n" \
               f"Livro 2: {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            _msg = ''

            for _n in range(other):
                _msg += '\n' + str(self)
            return _msg
        return "Impossível multiplicar"


livro1 = Livro("A Certain Magical Index, Vol. 17", "Kazuma Kamachi", 250)
livro2 = Livro("Seirei Tsukai no Blade Dance, Vol 1", "Shimizu Yuu", 186)

print(str(livro1))
print(str(livro2))

print(repr(livro1))
print(repr(livro2))

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

del livro1
del livro2
# Método __del__ sempre é chamado no encerramento do programa.

livro1 = Livro("A Certain Magical Index, Vol. 17", "Kazuma Kamachi", 250)
livro2 = Livro("Seirei Tsukai no Blade Dance, Vol. 1", "Shimizu Yuu", 186)
livro3 = Livro("Unlimited Fafnir, Vol. 5 ", "Tsukasa", 200)

print(livro1)
print(livro2)

print(livro1 + livro2)
print(livro3 * 3)
print(livro3 * livro1)
