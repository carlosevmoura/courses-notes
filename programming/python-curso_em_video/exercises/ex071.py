print('=' * 40)
print('{:^40s}'.format('BANCO CEV'))
print('=' * 40)

valor = int(input('Que valor você quer sacar? R$ '))

notas50 = valor // 50
notas10 = (valor % 50) // 10
notas1 = valor % 10

print('Total de {} cédulas de R$ 50.'.format(notas50))
print('Total de {} cédulas de R$ 10.'.format(notas10))
print('Total de {} cédulas de R$ 1.'.format(notas1))

print('=' * 40)

print('Volte sempre ao BANCO CEV!')