valor = float(input('Qual é o preço do seu produto? R$ '))
desconto = float(input('Qual é o desconto do seu produto? (%) '))

print('O produto que custava {:.2f}, com desconto de {:.2f} %, custará {:.2f}.'
    .format(valor, desconto, valor * ((100 - desconto) / 100)))