"""
Decoradores (Decorators)

 - Decoradores são funções;
 - Envolvem outras funções;
 - Servem para aprimorar funções;
 - Têm uma sintaxe própria, usando @ (não é obrigatório, mas torna mais agradável a leitura do código)

OBS.: Não confundir decorators com decorator function
"""
# Sintaxe não recomendada (sem Syntax Sugar):


def seja_educado(_funcao):
    def educacao():
        print("Foi um prazer te conhecer.")
        _funcao()
        print("Tenha um ótimo dia.")
    return educacao


def saudacao():
    print("Seja bem vindo")


def rage():
    print("VÁ À MERDA, PORRA!!!")


# Teste 1:
teste = seja_educado(saudacao)
print(teste())

# Teste 2:
bipolaridade = seja_educado(rage)
print(bipolaridade())

# Sintaxe recomendada (com Syntax Sugar):


def seja_educado(_funcao):  # Decorator function
    def educacao():
        print("Foi um prazer te conhecer.")
        _funcao()
        print("Tenha um ótimo dia.")
    return educacao


@seja_educado  # Decorator
def saudacao():
    print("Seja bem vindo")


@seja_educado
def rage():
    print("VÁ À MERDA, PORRA!!!")


# Não é mais necessário armazenar a função numa variável.
saudacao()
rage()
