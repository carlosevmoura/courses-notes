numero = int(input('Insira um número inteiro para obter a tabuada: '))

print('='*12)

contador = 1
for contador in range(1, 11):
    print('{} x {} = {}'.format(numero, contador, numero * contador))
    contador += 1

print('='*12)
