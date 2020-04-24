from random import choice
from emoji import emojize
from time import sleep

print("-=-"*10)
print('PEDRA, PAPEL OU TESOURA')
print("-=-"*10)

dicionarioEmoji = { 1 : emojize(':fist:', use_aliases=True),
                    2 : emojize(':hand:', use_aliases=True),
                    3 : emojize(':v:', use_aliases=True)}

print('[ 1 ] PEDRA {}'.format(dicionarioEmoji[1]))
print('[ 2 ] PAPEL {}'.format(dicionarioEmoji[2]))
print('[ 3 ] TESOURA {}'.format(dicionarioEmoji[3]))

user = int(input('Qual é a sua escolha? '))

if user not in [1, 2, 3]:
    print('Escolha uma opção válida neste jogo.')
    quit()

cpu = choice([1, 2, 3])

print('\nVamos lá!')
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('OU TESOOOURA!', end='\n\n')
sleep(2)

if user == cpu:
    print('Os dois escolheram {}! Empate!!!'.format(dicionarioEmoji[user]))
elif (user == 1 and cpu == 3) or (user == 2 and cpu == 1) or (user == 3 and cpu == 2):
    print('Você escolheu {} enquanto a máquina escolheu {}. Você venceu!!!'
          .format(dicionarioEmoji[user], dicionarioEmoji[cpu]))
else:
    print('Você escolheu {} enquanto a máquina escolheu {}. Você perdeu...'
          .format(dicionarioEmoji[user], dicionarioEmoji[cpu]))
