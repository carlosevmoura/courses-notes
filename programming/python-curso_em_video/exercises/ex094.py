from operator import itemgetter

lista = []
dados = {}

while True:
    dados['nome'] = input('Nome: ')

    while True:
        dados['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
        if dados['sexo'] in ['M', 'F']:
            break
        else:
            print('ERRO! Digite apenas M ou F!')

    dados['idade'] = int(input('Idade: '))

    lista.append(dados.copy())

    while True:
        resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resposta in ['S', 'N']:
            break
        else:
            print('ERRO! Por favor, responda apenas S ou N.')

    if resposta == 'N':
        break

print('-=' * 40)

print('A) Ao todo, temos {} pessoas cadastradas.'.format(len(dados)))

total = 0
for pessoa in lista:
    total += pessoa['idade']
media = total / len(lista)

print('B) A média de idade é de {} anos.'.format(media))

print('C) As mulheres cadastradas foram ', end=' ')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print('{}'.format(pessoa['nome']), end=' ')
print('.')

print('D) Lista das pessoas que estão acima da média de idade:')
for pessoa in lista:
    if pessoa['idade'] > media:
        for item, valor in pessoa.items():
            print('{} = {};'.format(item, valor), end=' ')
        print()

print('<< ENCERRADO >>')