import math

# Apresentação
print('Programa para calcular a distância e a altura')
print('atingida por um objeto lançado.')
print()

# Entradas
velocidade = float(input('Informe a velocidade de lançamento, em m/s: '))
angulo = float(input('Informe o ângulo de lançamento, em graus: '))

# Processamento
angulo_rad = math.radians(angulo)

altura_maxima = (velocidade * math.sin(angulo_rad)) ** 2 / (2 * 9.8)
distancia = velocidade ** 2 * math.sin(2 * angulo_rad) / 9.8

# Saídas
print('A altura máxima que o objeto atinge é:', altura_maxima)
print('A distância máxima que o objeto atinge é:', distancia)
