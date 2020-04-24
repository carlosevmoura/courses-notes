numero = int(input('Digite um número inteiro: '))
contador = 0

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print('\033[31m{}\033[0m'.format(divisor), end=' ')
        contador += 1
    else:
        print('\033[33m{}\033[0m'.format(divisor), end=' ')

if contador <= 2:
    print('\nO número {} não foi divisível nenhuma vez por números diferentes de 1 e dele mesmo.'
        .format(numero))
    print('Portanto, é um número primo!')
else:
    print('\nO número {} foi divisível {} vezes.'.format(numero, contador))
    print('Este número NÃO é um número primo.')