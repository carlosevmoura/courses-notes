print('========== LOJAS GUANABARA ==========')

valor = float(input('Preços das compras: R$ '))

print('\nFORMAS DE PAGAMENTO')
print('[ 1 ] À vista em dinheiro')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Duas parcelas no cartão')
print('[ 4 ] Três ou mais parcelas no cartão', end='\n\n')

forma = int(input('Selecione a forma de pagamento: '))

if forma == 1:
    print('O valor final de sua compra de R$ {:.2f} será de R$ {:.2f} com desconto.'
    .format(valor, valor * 0.9))
elif forma == 2:
    print('O valor final de sua compra de R$ {:.2f} será de R$ {:.2f} com desconto.'
          .format(valor, valor * 0.95))
elif forma == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(valor/2))
elif forma == 4:
    parcelas = int(input('Insira o número de parcelas: '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'
          .format(parcelas, valor * 1.2 / parcelas))
    print('Sua compra de R$ {:.2f} terá valor total de R$ {:.2f} ao término do pagamento.'
          .format(valor, valor * 1.2))
else:
    print('Esta forma de pagamento não é válida.')
