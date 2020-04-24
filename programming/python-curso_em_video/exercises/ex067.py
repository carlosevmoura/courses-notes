
while True:
    numero = int(input('Insira um número inteiro para obter a tabuada: '))
    if numero < 0:
        break

    print('='*12)

    for contador in range(1, 11):
        print('{} x {} = {}'.format(numero, contador, numero * contador))

    print('='*12)
