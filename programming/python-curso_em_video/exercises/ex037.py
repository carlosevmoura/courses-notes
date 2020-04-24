numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

base = int(input('Sua opção: '))

if   base == 1:
    print('O número {} na base binária é dado por {}.'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O número {} na base octal é dado por {}.'.format(numero, oct(numero)[2:]))
else:
    print('O número {} na base hexadecimal é dado por {}.'.format(numero, hex(numero)[2:]))
