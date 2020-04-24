from random import randint
from emoji import emojize
from time import sleep

print('-=-'*20)
print(emojize('Vou escolher um número entre 0 e 10. Tente adivinhar qual! :sunglasses:',
                    use_aliases=True))
print('-=-'*20)

numeroPy = int(randint(0, 10))

acertou = False
numeroUser = -1

while not acertou:
    tentativas += 1
    numeroUser = int(input('Qual foi o número que escolhi? '))

    if numeroUser == numeroPy:
        acertou = True
    elif numeroUser > numeroPy:
        print('É menor... Tente novamente! ')
    else:
        print('É maior... Tente novamente! ')

print('Parabéns! Você acertou após {} tentativas.'.format(tentativas))
