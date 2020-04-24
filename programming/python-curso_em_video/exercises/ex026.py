frase = input('Digite uma frase: ').strip().lower()

print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira aparição acontece na posição {}.'.format(frase.find('a') + 1))
print('A última aparição acontece na posição {}.'.format(frase.rfind('a') + 1))