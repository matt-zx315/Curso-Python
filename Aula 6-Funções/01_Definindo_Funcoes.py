"""
Funções são pequenos trechos de código que realizam tarefas específicas.
Podem receber, ou não, dados de entrada e retornar, ou não, dados de saída.
Muito úteis para executar procedimentos similares repetidas vezes.

OBS.: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a dunção seja simplificada.

Algumas funções já utilizadas:
-print()
-len()
-max()
-min()
-count()

Sintaxe:
def nome_da_função(parametro1, parametro2, ... ,parametroN):
    <bloco de código>
    return retorno

- Parâmetros são opcionais, sempre separados por vírgula caso hava mais de um.
- bloco de código: é onde o processamento da função acontece. É neste bloco que colocamos o retorno da função.
- retorno: também opcional. A função retorna o valor depois da palavra return. Usar apenas se houver retorno.

PEP-8 -> Nomes de função sempre devem ser escitos apenas com letras minúsculas
e separadas, em caso de nomes compostos, por underline (snake_case).
Funções também devem ter um espaço de duas linhas entre si e entre outras partes do código.
"""

# Exemplo de utilização
cores = ["laranja", "roxo", "verde", "azul", "amarelo", "vermelho", "marrom", "rosa", "branco", "preto"]
print(cores)  # Função que recebe dados.

texto = "Nepuru"
print(texto)

# texto.append("zugya") | retorna um erro porque string não possui o atributo append (AttributeError)

cores.clear()  # Função que não recebe dados.
print(cores)

# Princícipio DRY - Don't Repeat Yourself (Não se repita). Em programação, "Não Repita seu código".

# Definindo função (deixar duas linhas de espaço em branco antes e depois da função):


def dizer_oi():
    print("Oi")


"""
Observações sobre a função dizer_oi():

1) Usa outra(s) função(ões).
2) Só executa uma tarefa.
3) Não recebe parâmetro.
4) Não retorna nada.
"""

# Chamando função:
dizer_oi()


def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")


for i in range(5):
    cantar_parabens()

# Em Python, podemos criar variáveis de tipo função e executar como uma função.
canta = cantar_parabens()
canta
