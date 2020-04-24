frase = input('Digite uma frase: ').upper().strip().replace(' ','')

fraseInvertida = frase[::-1]

print('O inverso de {} é {}.'.format(frase, fraseInvertida))

if frase == fraseInvertida:
    print('Temos um palíndromo!')
else:
    print('NÃO temos um palíndromo...')