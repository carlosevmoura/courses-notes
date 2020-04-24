matrix = []
linha = []

for i in range(0,3):
    for j in range(0,3):
        linha.append(int(input('Digite um valor para [{}, {}]: '.format(i, j))))
    matrix.append(linha[:])
    linha.clear()

print('-=' * 20)
i = j = 0
while i < len(matrix):
    while j < len(matrix[i]):
        print('[{:^5}]'.format(matrix[i][j]), end=' ')
        j += 1
    print()
    j = 0
    i += 1