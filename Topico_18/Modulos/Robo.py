class Robo:
    def __init__(self, _nome, _bateria=100, _habilidades=[]):
        self.__nome = _nome
        self.__bateria = _bateria
        self.__habilidades = _habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar_bateria(self):
        self.__bateria = 100

    def diz_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'EU SOU {self.nome.upper()}.'
        return 'BATERIA FRACA. FAVOR CARREGAR!'

    def aprende_habilidade(self, _habilidade, _custo):
        if self.__bateria >= _custo:
            self.__bateria -= _custo
            self.__habilidades.append(_habilidade)
            return f'NOVA HABILIDADE APRENDIDA. {_habilidade.upper()}'
        return F'BATERIA INSUFICIENTE ({self.__bateria}/{_custo}). FAVOR CARREGAR!'
