# Apresentação
print('Programa para calcular a área de N retângulos')
print()

# Solicita a qtde de retângulos
qtde = int(input('De quantos retângulos deseja calcular a área? '))

for i in range(qtde):
    # Solicita os valores
    base = float(input('Informe a medida da base: '))
    altura = float(input('Informe a medida da altura: '))

    # Cálculo
    area = base * altura

    # Resultados na tela
    print('A área é', area)
    print('==========================')

