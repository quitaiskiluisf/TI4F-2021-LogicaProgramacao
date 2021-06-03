import math

def lancamento_obliquo_altura(velocidade, angulo):
    ''' Em uma situação de lançamento oblíquo,
        calcula a altura máxima que o objeto irá
        atingir. '''
    angulo_radianos = math.radians(angulo)
    return (velocidade * math.sin(angulo_radianos)) ** 2 / (2 * 9.8)


def lancamento_obliquo_distancia(velocidade, angulo):
    ''' Em uma situação de lançamento oblíquo,
        calcula a distância máxima que o objeto irá
        atingir. '''
    angulo_radianos = math.radians(angulo)
    return velocidade ** 2 * math.sin(2 * angulo_radianos) / 9.8


# Apresentação
print('Programa para calcular a altura máxima e a distância máxima percorrida')
print('por um projétil em uma situação de lançamento oblíquo.')
print()

# Entradas
velocidade_lancamento = float(input('Informe a velocidade de lançamento do objeto: '))
angulo_lancamento = float(input('Informe o ângulo de lançamento do objeto: '))

# Processamento
altura = lancamento_obliquo_altura(velocidade=velocidade_lancamento, angulo=angulo_lancamento)
distancia = lancamento_obliquo_distancia(velocidade=velocidade_lancamento, angulo=angulo_lancamento)

# Saídas
print('Altura máxima atingida:', altura)
print('Distância máxima atingida:', distancia)
