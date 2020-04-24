import math

catetoOposto = float(input('Insira o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Insira o comprimento do cateto adjacente: '))

print('A hipotenusa deste triângulo mede {:.2f}.'
    .format(math.hypot(catetoOposto, catetoAdjacente)))