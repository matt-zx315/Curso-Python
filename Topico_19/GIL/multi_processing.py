import time
from multiprocessing import Pool

CONTADOR = 50_000_000


def contagem_regressiva(_valor):
    while _valor > 0:
        _valor -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo de execução: {fim - inicio} segundos.')
