lista = []

while True:
    valor = int(input('Digite um valor inteiro: '))
    lista.append(valor)

    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 20)
print('Você digitou {} itens.'.format(len(lista)))

lista.sort(reverse=True)
print('Os valores em ordem decrescente são {}.'.format(lista))

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')