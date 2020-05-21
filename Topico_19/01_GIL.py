"""
GIL - Global Interpreter Lock

Recurso da linguagem Python que permite que apenas uma thread
funcione por vez.

Considerado como um recurso 'indecente' da linguagem.
"""
import sys

a = []
b = a
print(sys.getrefcount(a))  # 3 -> Duas referências das variáveis e uma da função

b = None
print(sys.getrefcount(a))  # 2 -> Uma referência da variável e outra da função.
