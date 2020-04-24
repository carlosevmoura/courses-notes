from datetime import date

anoNascimento = int(input('Insira o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    print('Quem nasceu em {}, completou {} anos em {}.'.format(anoNascimento, idade, anoAtual))
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('O alistamento será realizado em {}.'.format(anoNascimento + 18))
elif idade > 18:
    print('Quem nasceu em {}, completou 18 anos em {}.'.format(anoNascimento, anoNascimento + 18))
    print('O alistamento foi realizado em {}.'.format(anoNascimento + 18))
else:
    print('Quem nasceu em {}, completa 18 anos neste ano de {}!'.format(anoNascimento, anoAtual))
    print('O alistamento deve realizado este ano!')

