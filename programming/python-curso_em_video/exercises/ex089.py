alunos = []

while True:
    nome = str(input('Nome: '))
    notas = [float(input('Nota 1: ')),
             float(input('Nota 2: '))]

    alunos.append([nome, notas])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 20)

print('{:<4}{:<30}{:>6}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 40)

for item in range(len(alunos)):
    print('{:<4}{:<30}{:>6.1f}'
          .format(item,
                  alunos[item][0],
                  (alunos[item][1][0] + alunos[item][1][1])/2))

while True:
    print('-' * 40)
    aluno = int(input('Mostrar notas de qual aluno? ({} ou mais interrompe) '
                      .format(len(alunos)-1)))
    if (aluno == 999) or (aluno not in range(len(alunos))):
        break
    else:
        print('Notas de {} foram {}.'.format(alunos[aluno][0], alunos[aluno][1]))
