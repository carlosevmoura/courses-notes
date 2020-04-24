def fatorial(_numero = 1, show = False):
    resultado = 1
    for item in range(1, _numero + 1):
        resultado *= item

    if show:
        texto = ''
        for item in reversed(range(1, _numero + 1)):
            texto += '{} '.format(item)
            if item == 1:
                texto += '= {}'.format(resultado)
            else:
                texto += 'x '
    else:
        texto = '{}'.format(resultado)

    return texto

print(fatorial(5, True))
print(fatorial(5, False))

print(fatorial())