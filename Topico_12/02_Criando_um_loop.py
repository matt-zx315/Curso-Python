"""
Criando um loop customizado

"""
for numero in [1, 2, 3, 4, 5]:
    print(numero)

for letra in "Nepu":
    print(letra)


def loop_custom(_iteravel):
    _it = iter(_iteravel)

    while True:
        try:
            print(next(_it))
        except StopIteration:
            break


loop_custom("Nepu")
loop_custom([0, 1, 2, 3, 4, 5])
