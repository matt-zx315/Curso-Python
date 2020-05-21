"""
Tipagem dinâmica X tipagem estática

Tipagem dinâmica = atribuição de tipo apenas no momento da execução do código.
Podem ocorrer problemas durante a execução, como operações entre variáveis de
tipos diferentes por conta da atribuição dinâmica de valores (ex.: Soma de int
com string)

Tipagem estática = atribuição de tipo antes da verificação do valor atribuído.
Impede que valores diferentes do tipo sejam atribuídos à variável, bem como
interrompe o código caso encontre um valor de tipo diferente do attribuído.


"""
idade1 = 42  # Variável de tipo inteira com tipagem dinâmica (implícita)
print(type(idade1))

idade1 = "Quarenta e dois"  # Mudança do tipo de dado para string (atribuição de tipo de acordo com o dado)
