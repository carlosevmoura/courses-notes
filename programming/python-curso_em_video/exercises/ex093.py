jogador = {}
lista_gols = []

jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
for partida in range(partidas):
    lista_gols.append(int(input('\tQuantos gols na partida {}? '.format(partida + 1))))
    jogador['gols'] = lista_gols.copy()
    jogador['total'] = sum(lista_gols)

print('-=' * 30)
print(jogador)

print('-=' * 30)
for item, valor in jogador.items():
    print('O campo {} tem o valor {}.'.format(item, valor))

print('-=' * 30)
print('O jogador {} jogou {} partidas.'.format(jogador['nome'], len(jogador['gols'])))
for item, valor in enumerate(jogador['gols']):
    print('\t=> Na partida {}, fez {} gols.'.format(item + 1, valor))
print('Foi um total de {} gols.'.format(jogador['total']))