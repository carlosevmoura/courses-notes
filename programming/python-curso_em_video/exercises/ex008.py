medida = float(input('Insira a distância em metros: '))

print('A medida de {} m corresponde a:'.format(medida), end='\n\n')
print('> {:>8.4f}  km'.format(medida / 1000))
print('> {:>8.4f}  hm'.format(medida / 100))
print('> {:>8.4f} dam'.format(medida / 10), end='\n\n')
print('> {:>6.1f}  dm'.format(medida * 10))
print('> {:>6.1f}  cm'.format(medida * 100))
print('> {:>6.1f}  mm'.format(medida * 1000))