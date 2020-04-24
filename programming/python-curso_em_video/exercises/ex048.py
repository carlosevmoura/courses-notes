soma = 0
for numero in range(1, 501, 2):
    if numero % 3 ==0:
        soma += numero

print('O valor total obtido é de {}.'.format(soma))