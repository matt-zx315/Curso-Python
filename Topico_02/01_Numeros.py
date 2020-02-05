"""
Tipos numéricos

type(dado) -> Retorna o tipo do dado.

Não esquecer de, no código, utilizar print(type(dado))

No terminal não é necessário fazer isso. Apenas digitar
o comando já fará com que o tipo seja exibido na tela.

Podem ser inteiros (int), reais (float) ou complexos (complex)

- int: não possuem casas decimais.
- float: possui casas decimais.

Floats são separados por PONTO (.)
"""

# Soma (+)
print(5 + 7)

# Subtração (-)
print(6 - 2)

# Multiplicação (*)
print(3 * 4)

# Divisão com quociente real (/)
print(8 / 5)

# Divisão com quociente inteiro (//)
print(9 // 7)

# Resto da divisão (%)
print(7 % 3)

# Exponenciação (**)
print(8 ** 2)
"""
Curiosidade: enquanto em linguagens como Java um inteiro (int) possui um limite para seu tamanho,
no Python, esse limite é determinado apenas pela memória da máquina executando o programa.
Por exemplo: 2 ** 1000 em Java passaria da capacidade máxima permitida para um inteiro, mas em Python, o valor
é exibido normalmente. Partiu fazer contas com gugol XD
"""

# Separação de 3 em 3 casas com underline (1_000_000). Também funciona para casas decimais.
num = 1_874_962_032
print(num)
# Deixa a leitura BEM mais fácil

"""
Os dois casos abaixo diferem da seguinte forma:

O primeiro é uma variável numérica cujo valor recebe + 1 durante a operação. Seu valor original não é alterado.
Já no segundo caso ocorre um acréscimo e o valor da variável passa a ser seu valor inicial + 1. 
"""

num = 42
print(num + 1)

num += 1
print(num)
print(type(num))
# A operação acima também pode ser escrita num = num + 1.
# É possível ainda repetir a forma acima com outras operações.

num -= 1
print(num)
print(type(num))

num *= 3
print(num)
print(type(num))

num /= 6
print(num)
print(type(num))

num //= 5
print(num)
print(type(num))

num **= 2
print(num)
print(type(num))
# Divisões sempre retornam veriáveis de tipo float, a não ser que sejam feitas para retornar apenas inteiros.
# Usar // em um float irá retornar outro float.

# Separação de parte inteira e parte decimal.
valor = 1.44
print(valor)
print(type(valor))

"""
SE VOCÊ USAR VÍRGULA, NÃO HAVERÁ ERRO, MAS A VARIÁVEL ACABARÁ SAINDO COM OUTRO TIPO! (tupla)
Note, inclusive, que há um aviso de desrespeito da PEP8 ao escrever com a vírgula.
"""
valor = 1,44
print(valor)
print(type(valor))

# Vírgulas também podem ser usadas para múltiplas atribuíçoes
valor1, valor2, valor3, valor4 = 19, 10, 46, 67
print(valor1)
print(valor2)
print(valor3)
print(valor4)

# Por meio de casting, explicado em 06_Inputs.py, podemos converter float pra int, porém a parte decimal é perdida.
valor = 1.65
resultado = int(valor)
print(resultado)
print(type(resultado))

# Podemos trablhar, ainda, com números complexos (representados por 'j' em programação).
complexo = 5j
print(complexo)
print(type(complexo))
print(complexo ** 2)
print(complexo + 3)
print(complexo / 2)
# Todas as operações feitas até agora também são válidas para números complexos, EXCETO pela divisão com //.
