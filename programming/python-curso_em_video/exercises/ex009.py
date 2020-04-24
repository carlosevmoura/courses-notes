numero = int(input('Insira um número inteiro para obter a tabuada: '))

print('='*12)

contador = 1
while contador <= 10:
    print('{} x {} = {}'.format(numero, contador, numero * contador))
    contador += 1

print('='*12)
