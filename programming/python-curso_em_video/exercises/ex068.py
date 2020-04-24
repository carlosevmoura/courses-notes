from random import randint

print('=-=' * 14)
print('{:^42s}'.format('VAMOS JOGAR PAR OU ÍMPAR!'))
print('=-=' * 14)

vitorias = 0

while True:
    while True:
        numeroUser = int(input('Escolha o seu número (de 1 a 10): '))
        if numeroUser > 10 or numeroUser < 0:
            print('Número inválido. Escolha novamente!')
        else:
            break

    while True:
        escolhaUser = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        if escolhaUser not in ['P', 'I']:
            print('Opção inválida. Escolha novamente!')
        else:
            break

    numeroCPU = randint(0, 10)

    print('---' * 14)
    print('Você jogou {} e o computador jogou {}.'.format(numeroUser, numeroCPU))
    print('O total foi de {}!'.format(numeroUser + numeroCPU))
    print('---' * 14)

    if (numeroUser + numeroCPU) % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    if escolhaUser == resultado:
        print('Parabéns! Você VENCEU!!!')
        print('Vamos jogar novamente!')
        vitorias += 1
    else:
        print('A máquina venceu. Não foi dessa vez...')
        break

print('=-=' * 14)
print('GAME OVER!!! Você venceu {} vezes!'.format(vitorias))
