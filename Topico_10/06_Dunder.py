"""
Dunder main e dunder name

Dunder = Double Underline (__)

Dunder main -> __main__
Dunder name -> __name__

Dunders são utilizados em Python para criar classes, métodos, atributos etc.
para não gerar conflitos com os nomes.

# Na linguagem C, um programa é executado a partir da função:

int main(){
    return 0
}

# Em Java, a execução depende dessa mesma função:

public static void main(string[] args){

}

Em Python, a execução de um módulo diretamente na linha de comando, própria linguagem, internamente,
atribui à variável __name__ o valor __main__, indicando que este é o módulo de execução principal.
"""
from Topico_10.matrizes import *

matriz = gera_matriz()
nova = calcula_transposta(matriz)

imprime_matriz(matriz)
imprime_matriz(nova)



