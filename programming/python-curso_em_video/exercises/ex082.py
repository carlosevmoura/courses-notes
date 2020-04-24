lista = []

while True:
    valor = int(input('Digite um valor inteiro: '))
    lista.append(valor)

    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 20)
print('A lista completa é {}'.format(lista))

listaPares = []
listaImpares = []

for item in lista:
    if item % 2 == 0:
        listaPares.append(item)
    else:
        listaImpares.append(item)

print('A lista de pares é {}.'.format(listaPares))
print('A lista de ímpares é {}.'.format(listaImpares))