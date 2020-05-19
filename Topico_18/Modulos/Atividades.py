def comer(_comida, _saudavel):
    _final = ''

    if _saudavel:
        _final = 'porque é saudável.'
    else:
        _final = 'porque a gente só vive uma vez.'

    return f'Estou comendo {_comida} {_final}'


def dormir(_horas):
    _final = ''

    if _horas < 8:
        _final = f'Continuo cansado depois de dormir por {_horas} horas.'
    else:
        _final = f'Dormi demais! {_horas} horas de sono.'

    return _final


def eh_engracada(_pessoa):
    _comediantes = ['Faustão', 'Silvio Santos', 'Ari Toledo']
    if _pessoa in _comediantes:
        return True
    return False
