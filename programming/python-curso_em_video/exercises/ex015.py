dias = float(input('Insira o número de dias que o carro foi utilizado: '))
distancia = float(input('Insira a distância percorrida pelo carro, em quilômetros: '))

custoDias = float(input('Insira o custo por dia de utilização: R$ '))
custoDistancia = float(input('Insira o custo por quilômetro percorrido: R$ '))

print('O valor total a ser pago pelo carro alugado é de R$ {:.2f}.'
    .format(custoDias * dias + custoDistancia * distancia))

print('O valor relativo ao número de dias utilizados corresponde a R$ {:.2f} ({:.1f} %).'
    .format(custoDias * dias,
            100 * (custoDias * dias)/(custoDias * dias + custoDistancia * distancia) ))

print('O valor relativo a distância percorrida corresponde a R$ {:.2f} ({:.1f} %).'
    .format(custoDistancia * distancia,
            100 * (custoDistancia * distancia)/(custoDias * dias + custoDistancia * distancia) ))
