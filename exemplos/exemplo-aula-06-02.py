import math

def calcula_hipotenusa(cateto_oposto, cateto_adjacente):
    return math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)


# Apresentação
print('Programa para calcular a hipotenusa de um triângulo retângulo')
print()

# Entradas
op = float(input('Informe o valor da medida do cateto oposto: '))
ad = float(input('Informe o valor da medida do cateto adjacente: '))

# Processamento
hp = calcula_hipotenusa(cateto_oposto=op, cateto_adjacente=ad)

# Saída
print('O valor da hipotenusa é:', hp)
