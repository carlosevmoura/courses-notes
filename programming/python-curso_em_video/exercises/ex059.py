inicio = True
option = 4

while option != 5:
    if inicio == False:
        print("=-="*10)
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa')

        option = int(input('>>>>> Qual é a sua opção? '))

    if option == 1:
        print('A soma entre os números é {}.'.format(primeiroNumero + segundoNumero))
    elif option == 2:
        print('O produto entre os números é {}.'.format(primeiroNumero * segundoNumero))
    elif option == 3:
        if primeiroNumero > segundoNumero:
            print('O maior entre os números é {}.'.format(primeiroNumero))
        elif primeiroNumero < segundoNumero:
            print('O maior entre os números é {}.'.format(segundoNumero))
        else:
            print('Os dois números são iguais!')
    elif option == 4:
        if inicio == False:
            print('Insira os novos números: ')
        primeiroNumero = int(input('> Primeiro número: '))
        segundoNumero = int(input('> Segundo número: '))
    elif option == 5:
        print('Obrigado por utilizar este programa!')
    else:
       print('Esta opção não é válida. Escolha novamente.')

    inicio = False
