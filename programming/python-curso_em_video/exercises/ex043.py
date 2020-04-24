peso = float(input('Qual é o seu peso (em Kg)? '))
altura =  float(input('Qual é a sua altura (em cm)? '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
    print('O seu IMC é de {:.2f} e sua classificação é ABAIXO DO PESO.'.format(IMC))
elif IMC <= 25.0:
    print('O seu IMC é de {:.2f} e sua classificação é PESO IDEAL.'.format(IMC))
elif IMC <= 30.0:
    print('O seu IMC é de {:.2f} e sua classificação é SOBREPESO.'.format(IMC))
elif IMC <= 40.0:
    print('O seu IMC é de {:.2f} e sua classificação é OBESIDADE.'.format(IMC))
else:
    print('O seu IMC é de {:.2f} e sua classificação é OBESIDADE MÓRBIDA.'.format(IMC))
