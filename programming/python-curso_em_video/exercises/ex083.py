expressao = str(input('Digite a expressão: '))

listaAbreParenteses = []
listaFechaParenteses = []

for indice, caracter in enumerate(expressao):
    if caracter == '(':
        listaAbreParenteses.append(indice)
    elif caracter == ')':
        listaFechaParenteses.append(indice)

if len(listaAbreParenteses) != len(listaFechaParenteses):
    print('Sua expressão não é válida.')
else:
    for itemAbre in listaAbreParenteses[::-1]:
        for itemFecha in listaFechaParenteses:
            if itemFecha > itemAbre:
                listaFechaParenteses.remove(itemFecha)
    if listaFechaParenteses == []:
        print('Sua expressão é válida.')
    else:
        print('Sua expressão não é válida!')
