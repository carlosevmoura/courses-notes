velocidade = float(input('Qual é a velocidade atual do carro? '))
velocidadeLimite = 80.0

if velocidade > velocidadeLimite:
    print('MULTADO! Você excedeu o limite permitido de {:.1f} Km/h!'.format(velocidadeLimite))
    print('Você deve pagar uma multa de R$ {:.2f}.'.format((velocidade - velocidadeLimite) * 7))

print('Tenha um bom dia! Dirija com segurança!')