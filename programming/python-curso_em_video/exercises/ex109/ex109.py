from moeda import moeda, metade, dobro, aumentar, diminuir

numero = float(input('Digite o preço: R$ '))
print('A metade de {} é {}.'.format(moeda(numero), metade(numero, True)))
print('O dobro de {} é {}.'.format(moeda(numero), dobro(numero, True)))
print('Aumentando {}%, temos {}.'.format(15, aumentar(numero, 15, True)))
print('Diminuindo {}%, temos {}.'.format(15, diminuir(numero, 15, True)))
