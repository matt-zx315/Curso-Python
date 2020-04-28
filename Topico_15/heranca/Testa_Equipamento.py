from Topico_15.heranca.Equipamento import Equipamento
from Topico_15.heranca.Computador import Computador


class TestaEquipamento:
    equipamento = Equipamento("Roteador", 115026)
    computador = Computador("Computador", 105026, "i5 9400F", 16)

    @staticmethod
    def main():
        print(f"Dados do {TestaEquipamento.equipamento.tipo}:\n"
              f"Código: {TestaEquipamento.equipamento.codigo}\n"
              f"\n"
              f"Dados do {TestaEquipamento.computador.tipo}:\n"
              f"Código: {TestaEquipamento.computador.codigo}\n"
              f"CPU: {TestaEquipamento.computador.cpu}\n"
              f"RAM: {TestaEquipamento.computador.ram} GB\n")
