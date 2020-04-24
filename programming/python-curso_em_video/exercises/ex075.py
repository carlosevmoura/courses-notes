tupla = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais número: ')),
    int(input('Digite o último número: '))
)

print('Você digitou os valores: {}'.format(tupla))
print('O número 9 apareceu {} vezes.'.format(tupla.count(9)))
if 3 in tupla:
    print('O número 3 foi digitado pela primeira vez na pergunta {}.'.format(tupla.index(3)+1))
else:
    print('O número 3 não foi digitado.')

print('Os números pares digitados foram: ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
