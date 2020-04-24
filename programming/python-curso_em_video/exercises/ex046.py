from time import sleep

dicionario = {  1   : 'UM...',
                2   : 'DOIS...',
                3   : 'TRÊS...',
                4   : 'QUATRO...',
                5   : 'CINCUM...',
                6   : 'SEIX...',
                7   : 'SETE...',
                8   : 'OITO...',
                9   : 'NOVE...',
                10  : 'DEIX...',
                0   : 'E...'}

for contagem in range(10, -1, -1):
    print(dicionario[contagem])
    sleep(1)

print('PA PA PA...')
sleep(1)
print('PA PA PA PAAAA POU!!')
sleep(1)
print('PRA PRA POU! POU!')
sleep(2)
print('... POU!')