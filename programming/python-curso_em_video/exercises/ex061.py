print('=' * 40)
print('{:^40s}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)

inicio = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))

indice = 0
while indice < 10:
    print(inicio + razao * indice, end=' → ')
    indice += 1

print('... e acabou!')