def fatorial(numero):
    if numero > 1:
        return numero * fatorial(numero - 1)
    else:
        return 1

numero = int(input('Digite um número para calcular seu fatorial: '))
print('O valor da fatorial {}! é {}.'.format(numero, fatorial(numero)))