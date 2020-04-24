from datetime import date

trabalhador = {}

trabalhador['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
trabalhador['carteira'] = str(input('Carteira de Trabalho (0 se não possuir): '))

if trabalhador['carteira'] != '0':
    trabalhador['contrato'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] =  trabalhador['idade'] + \
                                    trabalhador['contrato'] + \
                                    35 - date.today().year

print('-=' * 20)

for item, valor in trabalhador.items():
    print('- {} tem o valor {};'.format(item, valor))
