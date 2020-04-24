def voto(_ano):
    from datetime import date
    idade = date.today().year - _ano

    if idade < 16:
        status = 'VOTO NEGADO'
    elif idade <= 18 or idade >= 70:
        status = 'VOTO OPCIONAL'
    else:
        status = 'VOTO OBRIGATÓRIO'
    return 'Para a idade de {}: {}'.format(idade, status)

print(voto(int(input('Insira o ano de nascimento: '))))