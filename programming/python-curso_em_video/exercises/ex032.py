from datetime import date

ano = input('Insira o ano que deseja analisar: ')

if ano == '':
    ano = date.today().year
else:
    ano = int(ano)

if ((ano % 100 != 0) and (ano % 4 == 0)) or ((ano % 100 == 0) and (ano % 400 == 0)):
    print('O ano {:.0f} é um ano bissexto.'.format(ano))
else:
    print('O ano {:.0f} NÃO é um ano bissexto.'.format(ano))