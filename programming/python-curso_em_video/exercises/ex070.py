print('-' * 30)
print('{:^30s}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

contador = totalValor = milValor = 0

while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))

    contador += 1
    totalValor += valor

    if valor > 1000:
        milValor += 1

    if (contador == 1) or (valor < menorValor):
        menorValor = valor
        menorValorNome = nome

    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break

print('FIM DO PROGRAMA')
print('O total da compra foi de R$ {:.2f}.'.format(totalValor))
print('Temos {} produtos custando mais de R$ 1000.00.'.format(milValor))
print('O produto mais barato foi {}, custando R$ {:.2f}.'.format(menorValorNome, menorValor))