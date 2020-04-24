import time

time_start, cpu_time_start = (time.time(), time.process_time())

tupla = ( 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'douze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
          'dezoito', 'dezenove', 'vinte'
        )

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    else:
        print('Este número não é válido. Digite novamente.')

print('Você digitou o número {}.'.format(tupla[numero]))

print("CPU time: {:.8f} s, wall time: {:.1f} s"
      .format(time.process_time() - cpu_time_start, time.time() - time_start))