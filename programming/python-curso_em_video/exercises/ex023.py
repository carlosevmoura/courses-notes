numeroStr = input('Digite um número 1 e 9999: ')

print('Analisando o número {}...'.format(numeroStr))
print('Milhar:  {}'.format(numeroStr[0]))
print('Centena: {}'.format(numeroStr[1]))
print('Dezena:  {}'.format(numeroStr[2]))
print('Unidade: {}'.format(numeroStr[3]), end='\n\n')

print('Agora utilizando as ferramentas matemáticas: ')
numeroInt = int(numeroStr)
print('Milhar:  {}'.format(numeroInt // 1000))
print('Centena: {}'.format(numeroInt // 100 % 10))
print('Dezena:  {}'.format(numeroInt // 10 % 10 ))
print('Unidade: {}'.format(numeroInt % 10))