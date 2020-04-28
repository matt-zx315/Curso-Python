from Topico_15.heranca.Equipamento import Equipamento


class Computador(Equipamento):
    def __init__(self, _tipo, _codigo, _cpu, _ram):
        super().__init__(_tipo, _codigo)
        self.__cpu = _cpu
        self.__ram = _ram

    @property
    def cpu(self):
        return self.__cpu

    @property
    def ram(self):
        return self.__ram

    @cpu.setter
    def cpu(self, _cpu):
        self.__cpu = _cpu

    @ram.setter
    def ram(self, _ram):
        self.__ram = _ram

    def exibe(self):
        print(f"Tipo: {self.tipo}\n"
              f"Código: {self.codigo}\n"
              f"CPU: {self.__cpu}\n"
              f"RAM: {self.__ram} GB\n")
