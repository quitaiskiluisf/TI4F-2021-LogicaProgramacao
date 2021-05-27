import math

# Apresentação
print('Programa para calcular as raízes')
print('de uma equação de segundo grau')
print()

# Entradas
a = float(input('Informe o valor do coeficiente A: '))
b = float(input('Informe o valor do coeficiente B: '))
c = float(input('Informe o valor do coeficiente C: '))

# Processamento e saídas
delta = (b ** 2) - (4 * a * c)

if (delta < 0):
    print('Esta equação não possui raízes reais.')
else:
    raiz = math.sqrt(delta)

    x1 = (-b - raiz) / (2 * a)
    x2 = (-b + raiz) / (2 * a)

    print()
    print('Valor do x1:', x1)
    print('Valor do x2:', x2)
