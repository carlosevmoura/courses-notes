valor = float(input('Insira o valor da casa: R$ '))
salario = float(input('Insira o salário do comprador: R$ '))
anos = int(input('Insira o tempo de financiamento (em anos): '))

parcela = valor / (anos * 12)

print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.'
      .format(valor, anos, parcela))

if parcela < 0.30 * salario:
    print('Empréstimo pode ser concedido!!!')
else:
    print('Empréstimo NEGADO!')