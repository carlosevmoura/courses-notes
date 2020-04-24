primeiroValor = int(input('Insira o primeiro número inteiro: '))
segundoValor = int(input('Insira o segundo número inteiro: '))
terceiroValor = int(input('Insira o terceiro número inteiro: '))

if (primeiroValor > segundoValor) and (primeiroValor > terceiroValor):
    maiorValor = primeiroValor
    if segundoValor > terceiroValor:
        menorValor = terceiroValor
    else:
        menorValor = segundoValor

if (segundoValor > primeiroValor) and (segundoValor > terceiroValor):
    maiorValor = segundoValor
    if primeiroValor > terceiroValor:
        menorValor = terceiroValor
    else:
        menorValor = primeiroValor

if (terceiroValor > primeiroValor) and (terceiroValor > segundoValor):
    maiorValor = terceiroValor
    if primeiroValor > segundoValor:
        menorValor = segundoValor
    else:
        menorValor = primeiroValor

print('O menor valor inserido foi {}.'.format(menorValor))
print('O maior valor inserido foi {}.'.format(maiorValor))