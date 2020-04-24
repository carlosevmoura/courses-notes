from random import randint

tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print('Os valores sorteados foram: {}'.format(tupla))
print('O maior valor sorteado foi: {}'.format(sorted(tupla)[-1]))
print('O menor valor sorteado foi: {}'.format(sorted(tupla)[0]))