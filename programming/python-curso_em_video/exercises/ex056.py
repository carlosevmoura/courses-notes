dicionario = {1: 'Primeira pessoa',
              2: 'Segunda pessoa',
              3: 'Terceira pessoa',
              4: 'Quarta pessoa'
              }

menor20anos = 0
idadeTotal = 0

for i in range(1, 5):
    print('=' * 40)
    print('{:^40s}'.format(dicionario[i]))
    print('=' * 40)

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    idadeTotal += idade

    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaiorIdade = nome

    if sexo == 'F' and idade < 20:
        menor20anos += 1

idadeMedia = idadeTotal / 4

print('A média de idade do grupo é de {} anos.'.format(idadeMedia))
print('O homem mais velho tem {} e se chama {}.'.format(maiorIdade, nomeMaiorIdade))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(menor20anos))