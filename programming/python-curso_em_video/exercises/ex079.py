lista = []

while True:
    valor = int(input('Digite um valor inteiro: '))
    if valor in lista:
        print('Valor duplicado! Não será adicionado...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')

    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 20)
print('Você digitou os valores {}'.format(lista))