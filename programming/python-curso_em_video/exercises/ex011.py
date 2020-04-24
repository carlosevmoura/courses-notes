largura = float(input('Insira a largura da parede (em metros): '))
altura = float(input('Insira a altura da parede (em metros): '))

print('Sua parede tem a dimensão de {:.2f}x{:.2f} m e sua área é de {:.2f} m^2.'
    .format(largura, altura, largura * altura))

print('Para pintar sua parede, serão necessários {:.2f} litros de tinta.'
    .format((largura * altura) / 2))