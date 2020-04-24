dicionario = {1: 'primeiro',
              2: 'segundo',
              3: 'terceiro',
              4: 'quarto',
              5: 'quinto',
              6: 'sexto',
              7: 'sétimo'
              }

menorPeso = 3000
maiorPeso = 0

for i in range(1, 6):
    peso = float(
        input('Insira o peso do {} indivíduo: '.format(dicionario[i])))

    if peso > maiorPeso:
        maiorPeso = peso
        maiorPesoIndice = i

    if peso < menorPeso:
        menorPeso = peso
        menorPesoIndice = i

print('O indivíduo de maior peso é o {}, com {} Kg.'
    .format(dicionario[menorPesoIndice], menorPeso))

print('O indivíduo de menor peso é o {}, com {} Kg.'
    .format(dicionario[maiorPesoIndice], maiorPeso))
