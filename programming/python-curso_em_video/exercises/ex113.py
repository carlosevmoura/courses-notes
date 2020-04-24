def leia_inteiro(_texto):
    while True:
        try:
            numero = int(input(_texto))
        except (ValueError, TypeError):
            print('>> Erro! O texto inserido não corresponde a um número inteiro válido.')
        except KeyboardInterrupt:
            print('>> Erro! O usuário não inseriu nenhum texto.')
        else:
            return numero


def leia_real(_texto):
    while True:
        try:
            numero = float(input(_texto))
        except (ValueError, TypeError):
            print('>> Erro! O texto inserido não corresponde a um número real válido.')
        except KeyboardInterrupt:
            print('>> Erro! O usuário não inseriu nenhum texto.')
        else:
            return numero


inteiro = leia_inteiro('Digite um número inteiro: ')
real = leia_real('Digite um número inteiro: ')

print('Você acabou de digitar o número inteiro {} e o número real {}.'.format(inteiro, real))
