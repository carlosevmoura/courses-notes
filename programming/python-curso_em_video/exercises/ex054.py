from datetime import date

dicionario = {1: 'primeiro',
              2: 'segundo',
              3: 'terceiro',
              4: 'quarto',
              5: 'quinto',
              6: 'sexto',
              7: 'sétimo'
              }

menorAno = 3000
maiorAno = 0
maioresIdade = 0
anoAtual = date.today().year

for i in range(1, 8):
    ano = int(
        input('Insira o ano de nascimento do {} indivíduo: '.format(dicionario[i])))

    if anoAtual - ano >= 18:
        maioresIdade += 1

    if ano > maiorAno:
        maiorAno = ano
        maiorAnoIndice = i

    if ano < menorAno:
        menorAno = ano
        menorAnoIndice = i

print('Ao todo, temos {} indivíduos maiores de idade e {} menores de idade.'.format(
    maioresIdade, 7 - maioresIdade))
print('O indivíduo de maior idade é o {}, nascido em {}.'.format(
    dicionario[menorAnoIndice], menorAno))
print('O indivíduo de menor idade é o {}, nascido em {}.'.format(
    dicionario[maiorAnoIndice], maiorAno))
