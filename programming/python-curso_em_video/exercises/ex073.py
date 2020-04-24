times = ('Flamengo', 'Santos', 'Palmeiras Não Tem Mundial', 'Grêmio', 'Afletico Paranaense',
'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vaxco da Gama',
'Atlético - MG', 'Fluminense - RJ', 'Botafogo - RJ', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense',
'Avaí')

print('-=' * 20)
print('Lista de times do Brasileirão: {}'.format(times))

print('-=' * 20)
print('Os cinco primeiros são: {}'.format(times[0:5]))

print('-=' * 20)
print('Os times rebaixados foram: {}'.format(times[-4::]))

print('-=' * 20)
print('A lista dos times em ordem alfabética {}'.format(sorted(times)))

print('-=' * 20)
print('O Flamengo terminou o campeonato na {}ª colocação.'.format(times.index('Flamengo') + 1))