def ficha(nome, gols):
    if not gols.isnumeric():
        gols = '0'
    if nome == '':
        nome = '<desconhecido>'
    print('O jogador {} marcou {} gol(s) no campeonato.'.format(nome, gols))

print('-' * 50)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

ficha(nome, gols)