import math

# Apresentação
print('Programa para calcular a área de um triângulo')
print()

# Entradas
lado_a = float(input('Informe a medida do lado A: '))
lado_b = float(input('Informe a medida do lado B: '))
angulo = float(input('Informe o ângulo formado entre o lado A e o lado B: '))

# Processamento
area = lado_a * lado_b  * math.sin(math.pi * angulo / 180) / 2

# Saídas
print('A área desse triângulo é:', area)
