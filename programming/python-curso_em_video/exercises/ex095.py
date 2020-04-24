jogadores = []
jogador = {}

while True:
    jogador['nome'] = input('Nome do Jogador: ')
    partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))

    lista_gols = []
    for partida in range(partidas):
        lista_gols.append(int(input('\tQuantos gols na partida {}? '.format(partida + 1))))
        jogador['gols'] = lista_gols.copy()
        jogador['total'] = sum(lista_gols)

    jogadores.append(jogador.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if resposta not in ['S','N']:
            print('Resposta inválida. Escolha S ou N.')
        else:
            break

    if resposta in 'N':
        break
    elif resposta in 'S':
        pass


print('-=' * 30)
print('{:>4} {:<30} {:<18} {:<5}'.format('cod', 'nome', 'gols', 'total'))

for cod, jogador in enumerate(jogadores):
    print('{:>4} {:<30} {:<18} {:<5}'
        .format(cod, jogador['nome'], str(jogador['gols']), jogador['total']))

while True:
    print('--' * 30)

    num = int(input('Mostrar dados de qual jogador? ({} ou maior para sair) '
                    .format(len(jogadores))))

    if num >= len(jogadores):
        break

    print(' {:-^60} '.format(' LEVANTAMENTO DO JOGADOR {} '.format(jogadores[num]['nome'].upper())))

    for item, valor in enumerate(jogadores[num]['gols']):
        print('\t=> Na partida {}, fez {} gols.'.format(item + 1, valor))
    print('Foi um total de {} gols.'.format(jogadores[num]['total']))

print('\n{:-^60}'.format(' FIM DO PROGRAMA '))