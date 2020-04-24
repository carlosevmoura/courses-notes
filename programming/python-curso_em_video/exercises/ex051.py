print('=' * 40)
print('{:^40s}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)

inicio = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))

for indice in range(0, 10):
    print(inicio + razao * indice, end=' → ')

print('... e acabou!')