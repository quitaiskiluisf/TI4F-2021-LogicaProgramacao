import math

def horizonte_de_radio(altura_torre):
    ''' Calcula o alcance esperado para o sinal de uma torre. '''
    return 4.12 * math.sqrt(altura_torre)


# Apresentação
print('Programa para calcular o alcance de um sinal emitido')
print('por uma torre, com base na altura desta torre.')
print()

# Entradas
altura = float(input('Informe a altura da torre, em m: '))

# Processamento
resultado = horizonte_de_radio(altura_torre=altura)

# Saídas
print()
print('A distância coberta por esta torre é de', resultado, 'km')
