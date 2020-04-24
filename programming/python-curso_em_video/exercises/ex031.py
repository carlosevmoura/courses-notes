distancia = float(input('Insira a distância da viagem em Km: '))

if distancia <= 200:
    print('O preço da passagem é de R$ {:.2f}.'.format(distancia * 0.50))
else:
    print('O preço da passagem é de R$ {:.2f}.'.format(distancia * 0.45))
