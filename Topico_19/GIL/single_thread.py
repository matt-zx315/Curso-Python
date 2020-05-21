import time

CONTADOR = 50_000_000


def contagem_regressiva(_valor):
    while _valor > 0:
        _valor -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo de execução: {fim - inicio} segundos.')
