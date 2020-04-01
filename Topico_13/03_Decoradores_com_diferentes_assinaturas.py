"""
Decoradores com diferentes assinaturas

Padrão de projeto Decorator Pattern (*args, **kwargs)

A assinatura de uma função é definida pelo seu retorno, nome e parâmetros de entrada.
"""
# Relembrando


def gritar(_funcao):
    def _aumentar(_nome):
        return _funcao(_nome).upper()
    return _aumentar


@gritar
def rage(_stress):
    return f"{_stress} disgraaaaçaaaaa"


@gritar  # Essa função não vai funcionar porque recebe 2 argumentos, enquanto gritar só recebe 1.
def rage_duplo(_stress1, _stress2):
    return f"{_stress1}, {_stress2} disgraaaaçaaaaa!!!!!!!!"


print(rage("oh porra"))

# Refatorando


def gritar(_funcao):
    def _aumentar(*args, **kwargs):
        return _funcao(*args, **kwargs).upper()
    return _aumentar


@gritar
def rage(_stress):
    return f"{_stress} disgraaaaçaaaaa"


@gritar
def rage_duplo(_stress1, _stress2):
    return f"{_stress1}, {_stress2} disgraaaaçaaaaa!!!!!!!!"


print(rage("oh porra"))
print(rage_duplo("tomar no cu", "se foder"))

# Decoradores com parâmetros de entrada:


def verifica_primeiro_argumento(_valor):
    def _interna(_funcao):
        def _outra(*args, **kwargs):
            if args and args[0] != _valor:
                return f"Valor incorreto. O primeiro valor precisa ser {_valor}."
            return _funcao(*args, **kwargs)
        return _outra
    return _interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(_num1, _num2):
    return _num1 + _num2


comida_favorita('pizza', 'churrasco', 'sorvete')
print(soma_dez(6, 4))
