def raiz_n(valor, indice):
    ''' Calcula a raiz do valor informado.
        O índice representa o índice da raiz. '''
    return valor ** (1 / indice)


# Apresentação
print('Programa para fazer o cálculo de raízes')
print()

# Entradas
valor = float(input('Informe o valor do qual deseja extrair a raiz: '))
indice = float(input('Informe o índice da raiz desejada: '))

# Processamento
resultado = raiz_n(valor, indice)

# Saídas
print('A raiz do valor é:', resultado)
