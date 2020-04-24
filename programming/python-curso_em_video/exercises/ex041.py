from datetime import date

anoNascimento = int(input('Insira o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print('O atleta possui {}.'.format(idade))

if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')
