print('-' * 60)
print('{:^60s}'.format('LISTA DE PREÇOS'))
print('-' * 60)

tupla = (
    ('Lápis', '1.75'),
    ('Borracha', '2.00'),
    ('Caderno', '15.90'),
    ('Estojo', '25.00'),
    ('Transferidor', '4.20'),
    ('Compasso', '9.99'),
    ('Mochila', '120.32'),
    ('Canetas', '22.30'),
    ('Livro', '34.90')
)

for item in tupla:
    print('{:.<51s}R${:>7s}'.format(item[0], item[1]))

print('-' * 60, end='\n')