"""
Geradores

 - Geradores (Generators) são Iteradores (Iterators);
 - Podem ser criados com funções geradoras;
 - Funções geradoras utilizam a palavra reservada yield;
 - Podem ser criados também com expressões geradoras;

Diferenças entre funções e funções geradoras (generator functions)

---------------------------------------------------------------------------------
|Funções                                |Funções Geradoras                      |
---------------------------------------------------------------------------------
|utilizam return                        |utilizam yield                         |
---------------------------------------------------------------------------------
|return encerra a função                |podem utilizar yield várias vezes      |
---------------------------------------------------------------------------------
|retorna um valor quando executada      |retorna um generator quando executada  |
---------------------------------------------------------------------------------

Em um generator, cada valor é gerado individualmente durante a execução da função.
Converer um gerador para lista fará com que todos os valores sejam gerados imediatamente.
"""
# Exemplo de função geradora


def conta_ate(_max):
    _cont = 1

    while _cont <= _max:
        yield _cont  # A função não se encerra após o yield
        _cont += 1


gen = conta_ate(5)

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)  # É preciso criar um gerador antes de cada uso.

for num in gen:
    print(num, type(num))

print('\nespaço vazio\n')

gen = conta_ate(5)
print(next(gen))  # 1

print('\nveja agora:')

for num in gen:
    print(num)  # 2 em diante.

lst = list(conta_ate(100))
print(lst)
