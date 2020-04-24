valor = float(input('Qual é o salário do trabalhador? R$ '))
aumento = float(input('Qual será o seu aumento? (%) '))

print('O trabalhador que recebia {:.2f}, com aumento de {:.2f} %, ganhará {:.2f}.'
    .format(valor, aumento, valor * (1 + aumento / 100)))