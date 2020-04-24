def aumentar(_valor, _percentual):
    return _valor * (1 + _percentual / 100)


def diminuir(_valor, _percentual):
    return _valor * (1 - _percentual / 100)


def dobro(_valor):
    return _valor * 2


def metade(_valor):
    return _valor / 2


def moeda(_valor):
    return 'R$ {:.2f}'.format(_valor).replace('.', ',')
