"""
Estruturas lógicas
and (E), or (OU), not (NÃO), is (É)

Operadores unários (trabalham com um único valor):
    - not
Operadores binários (comparam valores):
    - and, or, is

'and' necessita que todos os valores sejam verdadeiros.
'or' necessita que apenas um dos valores seja verdadeiro.
'not' inverte o valor, mudando de falso para verdadeiro e vice versa.
'is' compara objetos. Diferente do operador ==, que compara valores, 'is' compara as variáveis em si.

Podemos utilizar id(variável) para verificar o endereço de memória da variável. Se for o memso endereço,
'is' retornará True.
"""

ativo = True
logado = False

if ativo and logado:
    print("Bem vindo, usuário!")
elif ativo and not logado:
    print("Inicie a sessão.")
elif not ativo and logado:
    print("Você precisa ativar a conta.")
else:
    print("Crie uma conta para começar.")

if ativo or logado:
    print("Usuário existe.")
else:
    print("Usuário não encontrado.")

var1 = 5
var2 = 3
var3 = var1

if var1 == var2:
    print(True)
else:
    print(False)

if var1 is var2:
    print(True)
else:
    print(False)

if var1 is var3:
    print(True)
else:
    print(False)

print(id(var1))
print(id(var2))
print(id(var3))
# Como var3 aponta para o mesmo endereço de memória de var1, o operador 'is' retorna True.
