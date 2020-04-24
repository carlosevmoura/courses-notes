tupla =(
    'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
    'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'
)

for palavra in tupla:
    print('Na palavra {} temos'.format(palavra), end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print('{}'.format(letra), end=' ')
    print('')
