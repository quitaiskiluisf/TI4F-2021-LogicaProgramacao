# Apresentação
print('Programa para calcular a área de N retângulos')
print()

qtde = int(input('Qtde de retângulos desejados: '))

for i in range(1, qtde + 1):
    print('==========', i, 'º RETÂNGULO ==========')

    base = float(input('Informe a medida da base: '))
    altura = float(input('Informe a medida da altura: '))

    area = base * altura

    print('A área é', area)

