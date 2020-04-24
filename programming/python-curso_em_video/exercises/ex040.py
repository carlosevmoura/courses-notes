nota1 = float(input('A primeira nota do aluno é: '))
nota2 = float(input('A segunda nota do aluno é: '))
nota3 = float(input('A terceira nota do aluno é: '))
media = (nota1 + nota2 + nota3) / 3

print('A média das notas do aluno é {:.1f}.'.format(media))

if media >= 7.0:
    print('O aluno foi aprovado!')
elif media >= 3.0:
    print('O aluno fará recuperação.')
else:
    print('Eita. O aluno foi reprovado.')
