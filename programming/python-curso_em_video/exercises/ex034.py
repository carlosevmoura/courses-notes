salario = float(input('Insiria o valor do salário do trabalhador: R$ '))

if salario < 1250.00:
    print('O novo salário será de {:.2f}.'.format(salario * 1.15))
else:
    print('O novo salário será de {:.2f}.'.format(salario * 1.10))