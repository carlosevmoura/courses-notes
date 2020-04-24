numero = 0
contador = 0
total = 0

while numero != 999:
    numero = int(input('Insira um número [999 para parar]: '))
    if numero != 999:
        total += numero
        contador += 1

print('Foram inseridos {} números e a soma destes é {}.'.format(contador, total))