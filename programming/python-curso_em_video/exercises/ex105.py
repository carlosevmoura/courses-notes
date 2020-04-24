def notas(*notas, situacao = True):
    """Programa de análise de notas
    
    Keyword Arguments:
        situacao {bool} -- [Escolhe se realiza análise das notas] (default: {True})
    
    Returns:
        [dict] -- [Dados completos dos problema]
    """
    notas = list(notas)
    dados = {}
    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['média'] = sum(notas)/len(notas)

    if situacao == True:
        if dados['média'] < 5:
            dados['situação'] = 'RUIM'
        elif dados['média'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        elif dados['média'] < 9:
            dados['situação'] = 'BOA'
        else:
            dados['situação'] = 'EXCELENTE'
    return dados

resposta = notas(5.5, 2.5, 1.5, situacao = True)
print(resposta, end='\n\n')

print(notas.__doc__)