from random import randint
from emoji import emojize
from time import sleep

print('-=-'*20)
print(emojize('Vou escolher um número entre 0 e 5. Tente adivinhar qual! :sunglasses:',
                    use_aliases=True))
print('-=-'*20)

numeroPy = int(randint(1, 5))

numeroUser = int(input('Qual foi o número que escolhi? '))
print('Processando...')
sleep(3)

if numeroPy == numeroUser:
    print('Você ganhou! O número escolhido foi {}!'.format(numeroPy))
else:
    print('GANHEI! O número escolhido foi {} e não {}!'.format(numeroPy, numeroUser))