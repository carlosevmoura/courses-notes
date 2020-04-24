from random import randint
from time import sleep

def sorteia():
    print('Sorteando os números... ', end=' ', flush=True)
    sleep(0.5)
    lista = []
    for item in range(5):
        lista.append(randint(1,9))
        print(lista[-1], end=' ', flush=True)
        sleep(0.5)
    print('... e fim!')
    return lista

def somaPar(_lista):
    soma = 0
    for numero in _lista:
        if numero % 2 == 0:
            soma += numero
    print('Somando os valores em {}, temos {}.'.format(_lista, soma))

minha_lista = sorteia()
somaPar(minha_lista)