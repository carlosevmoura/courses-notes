def calcular_area(_largura, _comprimento):
    return _largura * _comprimento

print('\nControle de Terrenos')
print('-' * 20)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

print('A área de um terreno {:.1f} x {:.1f} é de {:.1f} m2.'
        .format(largura, comprimento, calcular_area(largura, comprimento)))