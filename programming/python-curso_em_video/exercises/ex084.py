maiorPesoNomes = []
menorPesoNomes = []
contador = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))

    if contador < 1:
        maiorPeso = peso
        menorPeso = peso
        maiorPesoNomes.append(nome)
        menorPesoNomes.append(nome)
    else:
        if maiorPeso < peso:
            maiorPeso = peso
            maiorPesoNomes.clear()
            maiorPesoNomes.append(nome)
        elif maiorPeso == peso:
            maiorPesoNomes.append(nome)

        if menorPeso > peso:
            menorPeso = peso
            menorPesoNomes.clear()
            menorPesoNomes.append(nome)
        elif menorPeso == peso:
            menorPesoNomes.append(nome)

    contador += 1

    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 20)
print('Ao todo, você cadastrou {} pessoas.'.format(contador))
print('O maior peso foi de {} Kg, de {}.'.format(maiorPeso, maiorPesoNomes))
print('O menor peso foi de {} Kg, de {}.'.format(menorPeso, menorPesoNomes))
