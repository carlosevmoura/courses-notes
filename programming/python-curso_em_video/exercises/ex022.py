nomeCompleto = input('Digite seu nome completo: ').strip()

print('Analisando o seu nome...')
print('Seu nome em letras maiúsculas é {}.'.format(nomeCompleto.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nomeCompleto.lower()))
print('Seu nome contém {} letras.'.format(len(nomeCompleto) - nomeCompleto.count(' ')))

nomePrimeiro = nomeCompleto.split()[0]
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nomePrimeiro, len(nomePrimeiro)))