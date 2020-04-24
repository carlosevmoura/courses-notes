nota1 = float(input('A primeira nota do aluno é: '))
nota2 = float(input('A segunda nota do aluno é: '))
media = (nota1 + nota2) / 2

print('A média das notas do aluno é {:.1f}.'.format(media))

if media > 7.0:
    print('O aluno foi aprovado!')
else:
    print('Eita. O aluno foi reprovado.')
