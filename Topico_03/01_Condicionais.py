"""
Estruturas condicionais
if, else e elif

- if: executa um bloco de código caso a(s) condição(ões) seja(m) verdadeira(s).
- else: executa um bloco de código no caso da(s) condição(ões) ser(em) falsa(s).
- elif: executa um novo bloco de código caso a(s) condição(ões) anterior(es) seja(m) falsa(s).
É necessário passar uma condição para o elif.
Podem ser utilizados quantos elifs forem necessários.

if e elif utilizam operadores de comparação:

< (menor que)
<= (menor ou igual a)
> (maior que)
>= (maior ou igual a)
== (igual a)
!= (diferente de)
"""

idade = 18

# if exige identação de 4 espaços após dois pontos. Tudo o que será executado pela condicional precisa estar identado.
# após encerrar o bloco de condicional, deixar uma linha vazia SEM IDENTAÇÃO (PEP8)
if idade < 18:
    print("Menor de idade.")
elif idade == 18:
    print("Tem 18 anos.")
else:
    print("Maior de idade.")
