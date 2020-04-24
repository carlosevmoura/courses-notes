cidade = input('Digite o nome da sua cidade: ')
cidadeInicio = cidade.split()[0]

if 'Santo' == cidadeInicio.capitalize():
    print('Sua cidade começa com a palavra Santo.')
else:
    print('Sua cidade começa NÃO com a palavra Santo.')
