matriz = []
linha = []

for i in range(0,3):
    for j in range(0,3):
        linha.append(int(input('Digite um valor para [{}, {}]: '.format(i, j))))
    matriz.append(linha[:])
    linha.clear()

print('-=' * 20)
i = j = 0
while i < len(matriz):
    while j < len(matriz[i]):
        print('[{:^5}]'.format(matriz[i][j]), end=' ')
        j += 1
    print()
    j = 0
    i += 1

print('-=' * 20)
somaPares = 0
for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
print('A soma dos valores pares é {}.'.format(somaPares))

somaColuna = 0
for i in range(0,3):
        somaColuna += matriz[i][2]
print('A soma dos valores da terceira coluna é {}.'.format(somaColuna))

linhaSegunda = matriz[1][:]
linhaSegunda.sort(reverse=True)
print('O maior valor da segunda linha é {}.'.format(linhaSegunda[0]))