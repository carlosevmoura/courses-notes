from math import fabs

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

primeiroSeg = float(input('Primeiro segmento: '))
segundoSeg  = float(input('Segundo segmento: '))
terceiroSeg = float(input('Terceiro segmento: '))

if ((fabs(segundoSeg  - terceiroSeg) < primeiroSeg < (segundoSeg  + terceiroSeg)) and
    (fabs(primeiroSeg - terceiroSeg) < segundoSeg  < (primeiroSeg + terceiroSeg)) and
    (fabs(primeiroSeg - segundoSeg)  < terceiroSeg < (primeiroSeg + segundoSeg))):
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
