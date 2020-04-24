from random import randint

lista = []
print('Valores sorteados:')
jogo = {}
for jogador in range(4):
    jogo['jogador'] = 'jogador' + str(jogador + 1)
    jogo['dado'] = randint(1, 6)
    lista.append(jogo.copy())
    print('{} tirou {} no dado.'.format(jogo['jogador'], jogo['dado']))

print('-=' * 20)

print('\n{:=^40}\n'.format(' RANKING DOS JOGADORES '))

lista_rankeada = sorted(lista, key=lambda k: k['dado'], reverse=True)

for posicao, jogo in enumerate(lista_rankeada):
    print('{}o lugar: {} com {}.'.format(posicao + 1, jogo['jogador'], jogo['dado']))
