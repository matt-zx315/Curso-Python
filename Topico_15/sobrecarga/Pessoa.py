class Pessoa:
    def __init__(self, _codigo=None, _nome=None, _idade=None):
        if _codigo is None or _nome is None or _idade is None:
            print("Construtor padrão")
        else:
            self.codigo = _codigo
            self.nome = _nome
            self.idade = _idade

    def exibe(self, _dado=1):
        if _dado == 1:
            print(f"Código: {self.codigo}\n"
                  f"Nome: {self.nome}\n"
                  f"Idade: {self.idade}\n")
        else:
            print(f"Código: {self.codigo}\n"
                  f"Nome: {self.nome}\n")


class TestaPessoa:
    fulano = Pessoa()
    ciclano = Pessoa("00157#ADF", "Ciclano", 19)

    fulano.codigo = "00164SCV"
    fulano.nome = "Fulano"
    fulano.idade = 16

    fulano.exibe()
    fulano.exibe(1)
    fulano.exibe("?")
    ciclano.exibe()
