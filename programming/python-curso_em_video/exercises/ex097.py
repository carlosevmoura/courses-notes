def escreva(_texto):
    largura = len(_texto) + 2
    print('~' * largura)
    print(' ' + '{}'.format(_texto) + ' ')
    print('~' * largura)

escreva('Minha função escreva() no Python!')
escreva('Curso em Vídeo com Gustavo Guabanara')