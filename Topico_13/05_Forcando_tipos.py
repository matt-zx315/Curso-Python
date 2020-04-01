"""
Forçando tipos de dados com decoradores


"""
# Declarando variáveis:

numero = 1
palavra = "palavra"


def forca_tipo(*_tipos):
    def _decorador(_funcao):
        def _converter(*args, **kwargs):
            _novo_args = []

            for (_valor, _tipo) in zip(args, _tipos):
                _novo_args.append(_tipo(_valor))

            return _funcao(*_novo_args, **kwargs)
        return _converter
    return _decorador


@forca_tipo(str, int)
def repete_mensagem(_mensagem, _vezes):
    for _vez in range(_vezes):
        print(_mensagem)


repete_mensagem(2, '4')
