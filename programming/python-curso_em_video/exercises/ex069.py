menor20anos = 0
homens = 0
maiorIdade = 0

while True:
    print('=' * 40)
    print('{:^40s}'.format('Cadastre uma pessoa'))
    print('=' * 40)

    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    if sexo == 'M':
        homens += 1

    if idade >= 18:
        maiorIdade += 1

    if sexo == 'F' and idade < 20:
        menor20anos += 1

    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if continua == 'N':
        break

print('Total de pessoas com mais de 18 anos: {}.'.format(maiorIdade))
print('Ao todo, temos {} homens cadastrados.'.format(homens))
print('E temos {} mulheres com menos de 20 anos.'.format(menor20anos))