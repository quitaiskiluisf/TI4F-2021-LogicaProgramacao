import math

def tan_deg(angulo):
    ''' Calcula a tangente de um ângulo. O ângulo fornecido em graus. '''
    return math.tan(math.radians(angulo))


def sin_deg(angulo):
    ''' Calcula o seno de um ângulo. O ângulo é fornecido em graus.'''
    return math.sin(math.radians(angulo))


def acos_deg(valor):
    ''' Calcula o arco cosseno de um ângulo. O retorno é um ângulo em graus.'''
    return math.degrees(math.acos(valor))


# Apresentação
print('Programa para calcular o percentual de luz do sol em um local e dia')

# Entradas
l = float(input('Informe a latitude: '))
da = int(input('Informe o número do dia do ano: '))

# Processamento e saídas
w = -tan_deg(l) * tan_deg(23.45 * sin_deg((360 * (284 + da)) / 365))

if (w < -1):
    print('Há sol o dia todo')
elif (w > 1):
    print('É noite o dia todo')
else:
    d = (2 * acos_deg(w) / (15 * 24)) * 100

    print(f'A porcentagem de luz solar é: {d:.2f}')