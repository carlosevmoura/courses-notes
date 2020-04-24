def aumentar(_valor, _percentual, _format = True):
    return moeda(_valor * (1 + _percentual / 100), _format)


def diminuir(_valor, _percentual, _format = True):
    return moeda(_valor * (1 - _percentual / 100), _format)


def dobro(_valor, _format = True):
    return moeda(_valor * 2, _format)


def metade(_valor, _format = True):
    return moeda(_valor / 2, _format)


def moeda(_valor, _format = True):
    if _format:
        return 'R$ {:.2f}'.format(_valor).replace('.', ',')
    else:
        return _valor
