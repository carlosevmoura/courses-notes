
sexo = input('Insira o sexo de uma pessoa (M/F): ').strip().upper()[0]

while sexo not in ['M','F']:
    sexo = input('Por favor, insira uma opção válida (M/F): ').strip().upper()[0]

print('Obrigado!')