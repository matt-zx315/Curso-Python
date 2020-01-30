from colored import *

texto = "%s Isso é um texto! %s" % (fg(208), attr(0))

print(texto)


def soma(_a, _b):
    return _a + _b


resultado = f"%s {soma(6, 4)} %s" % (fg(196), attr(0))

print(resultado)
