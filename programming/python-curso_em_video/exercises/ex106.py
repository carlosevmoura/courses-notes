def titulo():
    print('~' * 80)
    print('{:^80}'.format('Sistema Interativo PyHelp'))
    print('~' * 80)


def leia_comando():
    comando = str(input(
        '> Insira o comando que deseja obter ajuda: ("fim" para encerrar) ')).lower().strip()
    return comando


def imprimir_manual(_comando):
    try:
        print()
        help(_comando)
        print()
    except:
        pass


def encerramento():
    print('-' * 80)
    print('{:^80}'.format('Obrigado por utilizar o PyHelp!'))
    print('-' * 80)


while True:
    titulo()

    comando = leia_comando()

    imprimir_manual(comando)

    if comando == 'fim':
        encerramento()
        break
