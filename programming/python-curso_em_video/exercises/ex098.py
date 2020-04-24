from time import sleep

def contador(_inicio, _fim, _passo):
    for numero in range(_inicio, _fim + _passo, _passo):
        print('{}'.format(numero), end=' ', flush=True)
        sleep(1)
    print('FIM!')

print('=' * 40)
print('{:^40}'.format('Contando de 1 até 10!'))
contador(1, 10, 1)

print('=' * 40)
print('{:^40}'.format('Contando de 10 até 0, de 2 em 2!'))
contador(10, 0, -2)

print('=' * 40)
print('{:^40}'.format('Agora você escolhe!'))
user_inicio = int(input('Início: '))
user_fim = int(input('Fim: '))
user_passo = int(input('Passo: '))

contador(user_inicio, user_fim, user_passo)

print('\n=== FIM DO PROGRAMA ===')