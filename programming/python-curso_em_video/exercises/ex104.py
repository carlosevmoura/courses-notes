def leia_inteiro(_texto):
    while True:
        numero = str(input(_texto))
        if numero.isnumeric():
            return numero
        else:
            print('Erro! Digite um número inteiro válido!')

numero = leia_inteiro('Digite um número: ')
print('Você acabou de digitar o número {}.'.format(numero))
