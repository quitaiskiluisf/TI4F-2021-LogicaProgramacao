import math

# Apresentação
print('Programa para converter uma coordenada')
print('cartesiana para uma coordenada polar')
print()

# Entradas
x = float(input('Informe o valor da coordenada x: '))
y = float(input('Informe o valor da coordenada y: '))

# Processamento
r = math.sqrt(x ** 2 + y ** 2)
t = math.atan2(y, x)

# Saídas
print()
print('Este ponto é representado por')
print(f'r = {r:.4f}')
print(f't = {t:.4f}')
print('no sistema de coordenadas polares')
