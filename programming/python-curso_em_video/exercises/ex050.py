soma = 0

dicionario = {  1 : 'primeiro',
                2 : 'segundo',
                3 : 'terceiro',
                4 : 'quarto',
                5 : 'quinto',
                6 : 'sexto'
            }

for i in range(1, 7):
    numero = int(input('Insira o {} número: '.format(dicionario[i])))
    if numero % 2 == 0:
        soma += numero

print('A soma de todos os números pares dados é {}.'.format(soma))