"""
OBS.: Em algumas linguagens, dicionários Python são conhecidos como mapas.

Dicionários são coleções de dados do tipo chave : valor
São representados por chaves: dicionario = {chave: valor}

Tanto chaves quanto valores podem ser de qualquer tipo.
Não são indexados, ou seja, não possuem índice. Os acessos são feitos através das chaves.

Para adicionar ou atualizar elementos, as formas são as mesmas.
Dicionários NÃO aceitam chaves repetidas.
"""

print(type({}))

# Forma 1 (Mais comum para a criação de dicionários)
paises = {'br': "Brasil", 'us': "Estados Unidos", 'ag': "Argentina", 'de': "Alemanha"}
print(paises)

# Forma 2
paises = dict(br="Brasil", us="Estados Unidos", ag="Argentina", de="Alemanha")
print(paises)

# Acessando elementos:

# Forma 1 - Via chave, da mesma forma que lista/tupla
print(paises['br'])
# OBS.: Caso a chave seja inexistente, teremos o erro do tipo KeyError.

# Forma 2 - via get() (recomendado)
print(paises.get('us'))
print(paises.get('jp'))
# OBS.: get(chave) retorna None (sem tipo - vazio, ou null, em outras linguagens) caso não exista a chave.

pais = paises.get('de')

if pais:
    print("Encontrado")
else:
    print("Não encontrado")

# Ainda é possível criar um valor padrão para o caso de não existir a chave.

pais = paises.get('ru', "Não encontrado.")
print(f"País: {pais}")
pais = paises.get('ag', "Não encontrado.")
print(f"País: {pais}")

# Determinar se a chave existe no dicionário.
print('br' in paises)
print('as' in paises)
print('Alemanha' in paises)  # Não busca por valor, mas por chave.

if 'ru' in paises:
    pais = paises['ru']
else:
    print("Não encontrado.")

# Qualquer tipo de dado pode ser utilizado como chave, até mesmo listas, tuplas e até outros dicionários.
localidades = {
    (35.6895, 39.6917): "Escritório em Tóquio.",
    (40.7128, 74.0060): "Escritório em Nova Iorque.",
    (37.7749, 122.4194): "Escritório em São Paulo."
}

# Tuplas são bastante interessantes como chaves de dicionários por serem imutáveis.
print(localidades[(35.6895, 39.6917)])

# Adicionando elementos.
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

receita.update({'jun': 700})
print(receita)

# Atualizando dados - Forma 1.
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 500})
print(receita)

# Remover dados - Forma 1 -> pop(chave): precisamos informar a chave. Retorna KeyError se a chave não existir.
retorno = receita.pop('jun')  # Mais comum
print(retorno)
print(receita)

# Forma 2 -> del(chave)
del receita['fev']
print(receita)

# Métodos de dicionários
dicionario = dict(a=1, b=2, c=3, d=4)
print(dicionario)

# Limpar dicionário
dicionario.clear()

# Copiar dicionário (Deep Copy)
dicionario = dict(a=1, b=2, c=3, d=4)
novo = dicionario.copy()
novo['e'] = 4
print(novo)
print(dicionario)

# Copiar dicionário (Shallow Copy)
outro = novo
outro['f'] = 6
print(outro)
print(novo)

# Forma não usual de criação de dicionários.
d = {}.fromkeys('a', 5)
print(d)

# Atribuíção de um mesmo valor para várias chaves. Recebe um iterável (lista, tupla) e um valor.
usuario = {}.fromkeys(['nome', 'idade', 'e-mail', 'pontos'], "Desconhecido")
print(usuario)

# Uma string é lida como um iterável, gerando um conjunto de chaves (exceto caracteres repetidos).
string = {}.fromkeys('teste', 'valor')
print(string)

# Com range.
dicionario1 = {}.fromkeys(range(0, 10), "valor")
print(dicionario1)

# Iterar sobre dicionários
for chave in dicionario:
    print(chave)

for chave in dicionario:
    print(dicionario[chave])

for chave in paises:
    print(f"{chave} : {paises[chave]}")

print(paises.keys())  # Retorna uma lista de chaves

# Forma recomendada
for chave in paises.keys():
    print(paises[chave])

# Acessando os valores
print(paises.values())  # Retorna uma lista de valores

# Forma recomendada
for valor in paises.values():
    print(valor)

# Desempacotamento de dicionários.
for chave, valor in paises.items():
    print(f"Chave = {chave}; Valor = {valor}")

# Outras operações: Soma*, Valor Máximo*, Valor Mínimo*, Tamanho (*valores inteiros ou reais)
print(sum(dicionario.values()))
print(max(dicionario.values()))
print(min(dicionario.values()))
print(len(dicionario))