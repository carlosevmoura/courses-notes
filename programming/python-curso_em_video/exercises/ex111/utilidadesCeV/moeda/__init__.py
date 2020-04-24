def aumentar(_valor, _percentual, _format=True):
    return moeda(_valor * (1 + _percentual / 100), _format)


def diminuir(_valor, _percentual, _format=True):
    return moeda(_valor * (1 - _percentual / 100), _format)


def dobro(_valor, _format=True):
    return moeda(_valor * 2, _format)


def metade(_valor, _format=True):
    return moeda(_valor / 2, _format)


def moeda(_valor, _format=True):
    if _format:
        return 'R$ {:.2f}'.format(_valor).replace('.', ',')
    else:
        return _valor


def resumo(_valor, _aumento, _redução):
    print()
    print('-' * 40)
    print('{:^40}'.format('Tabela MoedaPy'))
    print('-' * 40)

    print('{:<30}{:}'.format('Preço analisado:', moeda(_valor)))
    print('{:<30}{:}'.format('Dobro do preço:', dobro(_valor)))
    print('{:<30}{:}'.format('Metade do preço:', metade(_valor)))
    print('{:<30}{:}'.format('{}% de aumento:'.format(_aumento),
                             aumentar(_valor, _aumento,)))
    print('{:<30}{:}'.format('{}% de redução:'.format(_redução),
                             diminuir(_valor, _redução,)))

    print('-' * 40)
