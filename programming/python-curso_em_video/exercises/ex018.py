import math

angulo = float(input('Digite o ângulo que você deseja: '))

print('O ângulo de {} possui os seguintes valores para as funções trigonométricas:'
    .format(angulo))

print('> Seno: {:.2f}'.format(math.sin(math.radians(angulo))))
print('> Cosseno: {:.2f}'.format(math.cos(math.radians(angulo))))
print('> Tangente: {:.2f}'.format(math.tan(math.radians(angulo))))