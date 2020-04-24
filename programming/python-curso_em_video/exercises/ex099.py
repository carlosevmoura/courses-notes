from time import sleep

def maior(*valores):
    print('-=' * 20)
    print('Analisando os valores...')

    if valores != ():
        for numero in valores:
            print('{}'.format(numero), end=' ', flush=True)
            sleep(0.1)

        print('\nForam informados {} valores ao todo.'.format(len(valores)))
        lista_decrescente = sorted(valores, reverse=True)
        print('O maior valor informado foi {}.'.format(lista_decrescente[0]))
    else:
        print('Nenhum valor foi informado.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()