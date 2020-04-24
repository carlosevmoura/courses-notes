import random

print('Digite o nome de cada um dos quatro alunos a serem sorteados:')
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

print('O aluno escolhido foi {}'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))