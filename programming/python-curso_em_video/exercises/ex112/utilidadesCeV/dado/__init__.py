def leia_dinheiro():
    while True:
        _valor = input('Digite o preço: R$ ')
        if _valor.isnumeric:
            return float(_valor)
        else:
            print('\033[33mERRO! Digite um valor válido!\033[0m')