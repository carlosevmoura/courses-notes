lista = []

for i in range(0, 5):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)
    lista.sort()
    indice = lista.index(numero)
    if numero == lista[-1]:
        print('O valor foi adicionado ao final da lista...')
    else:
        print('O valor foi adicionado na posição {} da lista...'.format(indice))

print('-=' * 20)
print('Os valores digitados em ordem foram {}'.format(lista))