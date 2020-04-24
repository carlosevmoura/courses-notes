from moeda import moeda, metade, dobro, aumentar, diminuir

numero = float(input('Digite o preço: R$ '))
print('A metade de {} é {}.'.format(moeda(numero), moeda(metade(numero))))
print('O dobro de {} é {}.'.format(moeda(numero), moeda(dobro(numero))))
print('Aumentando {}%, temos {}.'.format(15, moeda(aumentar(numero, 15))))
print('Diminuindo {}%, temos {}.'.format(15, moeda(diminuir(numero, 15))))
