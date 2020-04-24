print("-" * 40)
print('{:^40s}'.format('Sequência de Fibonacci'))
print("-" * 40)

termos = int(input('Quantos termos você quer mostrar? '))
contador = 1
valor1 = 0
valor2 = 1

while termos >= contador:
    if contador == 1:
        print('{}'.format(valor1), end=' → ')
        print('{}'.format(valor2), end=' → ')
        contador = 3
    fibonacci = valor1 + valor2
    print('{}'.format(valor1 + valor2), end=' → ')
    valor1 = valor2
    valor2 = fibonacci
    contador += 1
print('... e acabou!')