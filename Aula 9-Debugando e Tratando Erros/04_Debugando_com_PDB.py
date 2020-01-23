"""
Debugando com PDB

PDB = Python DeBugger

Bug -> Inseto

História do Debugging: No início da era da informática, um computador numa sala (na época eles ocupavam
salas inteiras) apresentou problemas na execução dos códigos. Quando entraram na sala, viram que uma mariposa
ficou presa nas válvulas e atrapalhava a saída de dados. Eis que foi realizado o primeiro debug da história:
tirar uma mariposa da sala do computador.

Uma prática não recomendada (mas recorrente) é o uso de print() para debugging.
Uma forma mais profissional de fazer isso é o uso do debugger. Em Python, o uso do
debbuger é possível em diversas IDEs, além da opção de se usar o PDB.

No PyCharm, basta clicar do lado do número das linhas que devem ser debugadas
depois clicar com o botão direito no código e selecionar a opção debug.
Também é possível selecionar trechos do código e, com o menu do botão direito,
selecionar Add to Watches, para ver os valores reotrnados.

Para utilizar o PDB, é necessário importar a biblioteca pdb e utilizar a função
set_trace()

Comandos básicos do PDB:

 l -> listar onde estamos no código
 n -> próxima linha
 p -> imprimir variável
 c -> continua a execução (finaliza o debug)

OBS.: No exemplo 2, o import do PDB é feito na mesma linha que a chamada da função set_trace().
Isso acontece porque no o debug é utilizado na fase de desenvolvimento. Por ser algo que será
removido mais à frente, essa prática, apesar de ir contra a PEP8, é realizada por questões de
praticidade. Não é necessário manter uma instrução que será removida mais adiante, portanto,
não é errado utilizá-la pontualmente e removê-la depois.

A partir do Python 3.7, não é mais necessário importar a biblioteca PDB, já que que o comando
debug foi incorporado como função built-in (integrada) chamada breakpoint

OBS.: CUIDADO COM NOMES DE VARIÁVEIS QUE SE CONFUNDAM COM OS COMANDOS DO PDB!
Para esses casos, utilizar o comando p.
Ainda assim, evitar o uso de nomes não representativos em variáveis.
Utilizar sempre nomes que sejam explicativos quanto ao que é a variável.
"""
import pdb


def dividir(_a, _b):
    try:
        return int(_a) / int(_b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema: {err}"


print(dividir(7, 4))

# # Exemplo 1 - Importando PDB e utilizando set_trace():
# nome = "Noé"
# sobrenome = "Dassua Konta"
# pdb.set_trace()
# nome_completo = nome + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso
# print(final)

# # Exemplo 2 - Importando e utilizando PDB na mesma linha:
# nome = "Noé "
# sobrenome = "Dassua Konta"
# import pdb; pdb.set_trace()  # Para executar dois comandos Python numa mesma linha, separá-los por ponto e vírgula (;)
# nome_completo = nome + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso
# print(final)

# # Exemplo 3 - Utilizando breakpoint():
# nome = "Noé "
# sobrenome = "Dassua Konta"
# breakpoint()  # Para executar dois comandos Python numa mesma linha, separá-los por ponto e vírgula (;)
# nome_completo = nome + sobrenome
# curso = "Programação em Python: Essencial"
# final = nome_completo + " faz o curso " + curso + "."
# print(final)

# Exemplo 4 - Conflitos entre variáveis e comandos:


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))