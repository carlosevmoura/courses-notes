lista =[]

for item in range(5):
    lista.append(int(input('Digite um valor para a posição {}: '.format(item))))

print('=-' * 30)

print('Você digitou os valores: {}'.format(lista))

copia = lista[:]
copia.sort()
maior = copia[-1]
menor = copia[0]

print('O maior valor digitado foi {} nas posições:'.format(maior), end='')
contador = 0
while maior in lista[contador:]:
    indice = lista.index(maior, contador)
    print(' {}'.format(indice), end='')
    contador = indice + 1
print('.')

print('O menor valor digitado foi {} nas posições:'.format(menor), end='')
contador = 0
while menor in lista[contador:]:
    indice = lista.index(menor, contador)
    print(' {}'.format(indice), end='')
    contador = indice + 1
print('.')