import math

def converte_ntc_para_celsius(resistencia):
    ''' Converte a resistência fornecida por um termistor
    NTC para uma temperatura em Graus Celsius. '''
    return 1 / (298.15 ** -1 + (3950 ** -1) * math.log10(resistencia / 10000)) - 273.15


#  Apresentação
print('Programa para converter a resistência fornecida por um termistor NTC')
print('em uma temperatura em graus Celsius.')
print()

# Entradas
r = float(input('Informe o valor da resistência:'))

# Processamento
resultado = converte_ntc_para_celsius(resistencia=r)

# Saídas
print()
print('A temperatura é:', resultado, '°C')
