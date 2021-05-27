import math

# Apresentação
print('Programa para calcular a temperatura')
print('com base na resistência apresentada por um termistor')
print('do tipo NTC.')
print()

# Entradas
resistencia = float(input('Informe a resistência apresentada pelo termistor: '))

# Processamento
resultado = 1 / (298.15 ** -1 + (3950 ** -1) * math.log10(resistencia / 10000)) - 273.15

# Saídas
print('O resultado é:', resultado, '°C')
