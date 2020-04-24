numero = int(input('Digite um número para calcular seu fatorial: '))

fatorial = 1
item = numero

while item > 0:
    fatorial = fatorial * item
    item += -1

print('O valor da fatorial {}! é {}.'.format(numero, fatorial))