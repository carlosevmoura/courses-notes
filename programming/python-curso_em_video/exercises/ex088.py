from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGANDO NA MEGA SENA'))
print('-' * 30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('{:-^30}'.format('SORTEANDO {} JOGOS'.format(jogos)))

jogo = 1
while jogo < jogos:
    sleep(1)
    aposta = []
    for i in range(0,7):
        while True:
            numero = randint(1, 60)
            if numero not in aposta:
                aposta.append(numero)
                break
    aposta.sort()
    print('Jogo {}: {}'.format(jogo, aposta))
    aposta.clear()
    jogo += 1

print('{:-^30}'.format(' BOA SORTE '))
