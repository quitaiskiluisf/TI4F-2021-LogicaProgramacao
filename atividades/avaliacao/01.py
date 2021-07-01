# Apresentação
print('Programa para calcular a média harmônica')
print('de 4 valores')
print()

# Entradas
n1 = float(input('Informe o valor 1: '))
n2 = float(input('Informe o valor 2: '))
n3 = float(input('Informe o valor 3: '))
n4 = float(input('Informe o valor 4: '))

# Processamento
resultado = 4 / ((1 / n1) + (1 / n2) + (1 / n3) + (1 / n4))

# Saídas
print(f'A média harmônica é {resultado:.3f}')
