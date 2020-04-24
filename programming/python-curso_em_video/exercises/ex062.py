print('=' * 40)
print('{:^40s}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)

inicio = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))

total = 0
termos = 10

while termos > 0:
    indice = 0
    while indice < termos:
        print(inicio + razao * indice, end=' → ')
        indice += 1
    print('...')
    inicio = inicio + razao * indice
    total += termos
    termos = int(input('Quantos termos você quer mostrar a mais? '))

print('A progressão foi finalizada com {} termos calculados.'.format(total))