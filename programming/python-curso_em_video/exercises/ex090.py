aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média de {}: '.format(aluno['nome'])))

if aluno['media'] >= 7.0:
    aluno['status'] = 'aprovado'
elif aluno['media'] >= 3.0:
    aluno['status'] = 'recuperação'
else:
    aluno['status'] = 'reprovado'

print('-=' * 20)

for chave, valor in aluno.items():
    print('- {}: {}'.format(chave, valor))