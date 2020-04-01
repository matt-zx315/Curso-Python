"""
Criando um iterador customizado

OBS.: Será necessário usar alguns conceitos de programação orientada a objetos (POO).
"""
for i in range(11):
    print(i)


class Contador:
    def __init__(self, _menor, _maior):
        self.maior = _maior
        self.menor = _menor

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            _numero = self.menor
            self.menor += 1
            return _numero
        raise StopIteration


cont = Contador(1, 6)  # Nesse caso, podemos apenas chamar o método next() 5 vezes.

it1 = iter(cont)

print(next(it1))

for i in Contador(0, 11):
    print(i)
