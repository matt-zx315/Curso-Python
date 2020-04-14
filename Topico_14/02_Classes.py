"""
POO - Classes

Em POO, classes nada mais são do que modelos dos objetos do mundo real
sendo representados computacionalmente.

Contextualizando: um sistema para automatizar o controle de lâmpadas
em uma casa. As lâmpadas são os objetos representados. Como esse objeto
não existe na linguagem Python (e nem em nenhuma outra, possivelmente),
ele será representado como uma classe no sistema.

OBS.: Durante o planejamento do software, após serem definidas as classes que estarão no
sistema, esses objetos do mundo real mapeados para o sistema são chamados de entidades.

Classes podem conter:

    -Atributos: características do objeto. Permitem a representação computacional dos estados do objeto.
    Ex.: Tensão da lâmpada, luminosidade, cor, estado (acesa ou apagada) etc;

    -Métodos (funções): Representam as ações que o objeto pode executar no programa.
    Ex.: Apagar/Acender, regular luminosidade, modo (acesa, piscando devagar etc.) entre outros;

Em Python, a palavra reservada class é utilizada para representar uma classe. A inicial do nome
da classe é, por convenção, maiúscula. Caso seja um nome composto, as iniciais são com letras
maiúsculas, com as palavras juntas (ex.: ContaCorrente). Isso permite diferenciar as classes
criadas pelo desenvolvedor das classes internas da linguagem.

Também é possível criar várias classes em um único arquivo, bem como não é necessário
que o arquivo tenha o mesmo nome da classe principal.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp1 = Lampada()

print(type(Lampada))
