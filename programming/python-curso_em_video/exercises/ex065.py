resposta = 'S'
total = maior = menor = contador = 0

while resposta != 'N':
    numero = int(input('Insira um número: '))

    total += numero

    if numero > maior:
        maior = numero

    if contador == 1:
        menor = numero
    elif numero < menor:
        menor = numero

    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    contador += 1

print('Você digitou {} números e a média foi {}.'.format(contador, total/contador))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))