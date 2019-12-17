"""
Tipo string

Em Python, string é tudo que estiver entre:
"""

# - Aspas simples -> 'string', 'z', '36'
texto = 'nepu'
print(texto)
print(type(texto))

# - Aspas duplas -> "string", "z", "36"
texto = "nepu"
print(texto)
print(type(texto))

# - Aspas simples triplas -> '''string''', '''z''', '''36'''
texto = '''nepu'''
print(texto)
print(type(texto))

# - Aspas duplas triplas -> """string""", """z""", """36"""
texto = """nepu"""
print(texto)
print(type(texto))

"""
Se por qualquer motivo for necessário o uso de aspas dentro da string fazer o seguinte:

- Se precisar utilizar aspas duplas, coloque a string entre aspas simples;
- Se precisar utilizar aspas simples, coloque a string entre aspas duplas.
"""
texto = 'Ele então disse: "Isso vai dar uma confusão...".'
print(texto)
texto = "João's Bar"
print(texto)

"""
Formatação de texto e caracteres de escape:
 
 \n é utilizado para quebra de linha, exibindo tudo o que estiver depois deste marcador na linha seguinte.
 É importante lembrar que strings contam os espaços como caracteres, sem contar que, visualmente, o uso de
 \n pode ficar um tanto desagradável. Uma solução é utilizar aspas duplas triplas e separar o texto por linhas.
 Nesse caso, também se torna possível utilizar aspas simples e aspas duplas dentro da string.
 
 Há outra forma ainda. Ao colocar um texto entre aspas duplas (exemplo = "Uma mensagem qualquer."),
 pode-se usar \ fora das aspas e começar uma nova linha. Para inserir a quebra, é só usar \n.
 
 Um aviso: não identar o texto dentro da string pra ficar bonito no código, ou a identação
 aparecerá na saída do programa. Siga o terceiro exemplo abaixo.
 
 Segue uma lista de carcteres de escape e suas funções
 
 \\ -> imprime barra invertida (backlash) na string
 \' -> imprime aspas simples
 \" -> imprime aspas duplas
 \a -> aciona um bipe, se houver suporte
 \b -> apaga o caractere anterior a este
 \f -> insere quebra de página
 \n -> quebra de linha
 \r -> equivalente ao efeito da tecla Enter
 \u2600 -> insere um caractere UNICODE. 2600 é um sol. Usar tabela de referência para outros símbolos.
 \t -> tabulação horizontal
 \v -> tabulação vertical
 
 tabela de emojis: https://apps.timwhitlock.info/emoji/tables/unicode
"""

texto = "Fusca\nAzul"
print(texto)

texto = "Ele então disse: \"Isso vai dar uma confusão...\"."
print(texto)

texto = """O fusca azul parou em frente ao João's Bar.
O balconista viu aquilo e disse: "Isso vai dar uma confusão..."."""
print(texto)

texto = "nepu puru"

texto = texto.upper()  # todos os caracteres maiúsculos
print(texto)

texto = texto.lower()  # todos os caracteres minúsculos
print(texto)

print(texto.split())  # cria uma lista de strings, com cada elemento da lista sendo uma palavra antes dos espaços

print(texto[0:4])  # slice de string. Toda string é uma lista, inclusive.
print(texto.split()[1])  # O número entre colchetes indica qual a posição do elemento da lista será acessado.
print(texto[3])  # Acessar caractere específico da string.
print(texto[:: -1])  # Começa do primeiro elemento, vai até o último e inverte o texto
print(texto[: -1])  # Apresenta a string toda, excluindo o último caractere do texto
print(texto[0: 9])  # Percorre a string do elemento inicial (0) até o elemento final (8 ou 9 - 1)
# Apesar de serem listas, strings não podem utulizar o método reverse()

print(texto.replace('p', 't'))  # Substitui caracteres antes da vírgula pelos caracteres depois da vírgula.
print(texto.replace('nepu puru', 'uzu gya'))  # Pode ser usado para substituir trechos inteiros da string.
print(texto + ", uzu, gya")  # Sinal de operação + é usado para concatenar (adicionar) texto à string.
num = str(96)  # Função de cast para conversão de variável para string.
print(type(num))

texto = "Pimba "
print(texto * 3)  # Textos em Python podem ser multiplicados, aparecendo diversas vezes.
