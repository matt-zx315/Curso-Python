"""
Conjuntos, em qualquer linguagem de programação, é uma referência
à teoria dos conjuntos da matemática.

Em Python, conjuntos são chamados de Sets.

Da mesma forma que na matemática:

-Sets não possuem valores duplicados;
-Sets não possuem valores ordenados;
-Elementos não são acessados via índice (não indexados);

Conjuntos são bons para se utilizar quando precisamos armazenar
elementos, mas não nos importamos com a ordenação deles. Quando
não precisamos nos preocupar com chaves, valores e itens duplicados.

São representados por chaves: conjunto = {}

Diferenças entre conjuntos e mapas/dicionários:

-Um dicionário tem chave e valor.
-Conjunto tem apenas o valor.
"""

# Forma 1:
conjunto = set({0, 1, 2, 1, 3, 4, 3, 6, 9, 8, 7, 5, 5, 6, 4, 9})
print(conjunto)  # Valores repetidos não são inseridos no conjunto e também não geram erros.
print(type(conjunto))

# Forma 2 (mais comum):
conjunto = {0, 1, 2, 1, 3, 4, 3, 6, 9, 8, 7, 5, 5, 6, 4, 9}
print(conjunto)
print(type(conjunto))


# Convertendo outras coleções em conjuntos.
conjunto = "Nepuruzugya"
conjunto = set(conjunto)
print(conjunto)  # Conjuntos, ao serem criados com a função set(coleção), apresentam elementos desordenados.
print(type(conjunto))

cores = ["laranja", "roxo", "verde", "azul", "amarelo", "vermelho", "marrom", "rosa", "branco", "preto"]

conjunto = set(cores)
print(conjunto)
print(type(conjunto))

tupla = tuple(range(10))

conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

n = 12
if n in conjunto:
    print(f"{n}: Encontrado.")
else:
    print(f"{n}: Não encontrado.")

# Não há ordem nem valores repedidos em um conjunto, diferente de outras coleções.
lista = [99, 25, 64, 87, 36, 11, 11, 25, 87, 47, 21, 32, 21, 32, 65, 65]
print(f"lista: {lista}\nTamanho = {len(lista)}\n{type(lista)}")

tupla = (99, 25, 64, 87, 36, 11, 11, 25, 87, 47, 21, 32, 21, 32, 65, 65)
print(f"tupla: {tupla}\nTamanho = {len(tupla)}\n{type(tupla)}")

dicionario = {}.fromkeys([99, 25, 64, 87, 36, 11, 11, 25, 87, 47, 21, 32, 21, 32, 65, 65], 'dict')
print(f"dicionário: {dicionario}\nTamanho = {len(dicionario)}\n{type(dicionario)}")

conjunto = {99, 25, 64, 87, 36, 11, 11, 25, 87, 47, 21, 32, 21, 32, 65, 65}
print(f"conjunto: {conjunto}\nTamanho = {len(conjunto)}\n{type(conjunto)}")

# Podemos misturar tipos de dados.
c = {1, True, "Água", 16.5}
print(c)
print(type(c))

# Iterando em um conjunto.
for n in conjunto:
    print(n, end=" ")

print()

# Adicionando elementos.
conjunto.add(93)
conjunto.add(93)  # Adicionar um valor igual não gera erro. Apenas é ignorado.
print(conjunto)

# Removendo elemento. Remove o valor.
conjunto.remove(11)  # Forma 1. Se o valor não existir, retorna um KeyError. Não retorna o valor removido.
print(conjunto)

conjunto.discard(65)  # Forma 2. Não gera erro caso o parâmetro passado não exista no conjunto.
print(conjunto)

# Copiando conjuntos.

novo = conjunto.copy()  # Deep Copy
novo.add(16)
print(novo)
print(conjunto)
print(novo is conjunto)

outro = novo  # Shallow Copy
outro.add(77)
print(outro)
print(novo)
print(outro is novo)

# Métodos matemáticos
estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Gerar um conjunto único. OBS.: NÃO É POSSÍVEL CONCATENAR CONJUNTOS!
uniao1 = estudantes_python.union(estudantes_java)  # Forma 1: Método union(conjunto).
print(uniao1)

uniao2 = estudantes_python | estudantes_java  # Forma 2: caractere | (pipe)
print(uniao2)

# Encontrando elementos em comum.
interseccao1 = estudantes_python.intersection(estudantes_java)  # Forma 1: Método intersection(conjunto)
print(interseccao1)

interseccao2 = estudantes_python & estudantes_java  # Forma 2: caractere & ('E' comercial)
print(interseccao2)

# Encontrando elementos que pertencem apenas a um conjunto.
diferenca_python = estudantes_python.difference(estudantes_java)  # Método difference(conjunto)
print(diferenca_python)

diferenca_java = estudantes_java.difference(estudantes_python)
print(diferenca_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho. (*Apenas para conjuntos com valores reais e/ou inteiros apenas)
print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))