from math import fabs

print('-=-' * 20)
print('Analisador de Triângulos 2.0')
print('-=-' * 20)

primeiroSeg = float(input('Primeiro segmento: '))
segundoSeg  = float(input('Segundo segmento: '))
terceiroSeg = float(input('Terceiro segmento: '))

if ((fabs(segundoSeg  - terceiroSeg) < primeiroSeg < (segundoSeg  + terceiroSeg)) and
    (fabs(primeiroSeg - terceiroSeg) < segundoSeg  < (primeiroSeg + terceiroSeg)) and
    (fabs(primeiroSeg - segundoSeg)  < terceiroSeg < (primeiroSeg + segundoSeg))):

    if primeiroSeg == segundoSeg == terceiroSeg:
        print('Os segmentos acima PODEM formar um triângulo equilátero.')
    elif (primeiroSeg == segundoSeg) or (primeiroSeg == terceiroSeg) or (segundoSeg == terceiroSeg):
        print('Os segmentos acima PODEM formar um triângulo isósceles.')
    else:
        print('Os segmentos acima PODEM formar um triângulo escaleno.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
