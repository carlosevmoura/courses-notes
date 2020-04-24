pares = []
impares = []
numeros = [pares , impares]

for i in range(1, 8):
    numero = int(input('Digite o {}o. valor: '.format(i)))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()
print('-='*20)
print('Os valores pares digitados foram: {}.'.format(pares))
print('Os valores ímpares digitados foram: {}.'.format(impares))