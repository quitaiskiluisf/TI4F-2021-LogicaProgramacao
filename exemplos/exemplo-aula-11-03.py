# Apresentação
print('Programa para cálculo da área de 3 retângulos')
print()

for i in range(3):
    # Solita as medidas do retângulo
    base = float(input('Informe o valor da base do retângulo: '))
    altura = float(input('Informe o valor da altura do retângulo: '))

    # Cálculo
    area = base * altura

    # Apresenta o resultado
    print('A área é:', area)
    print('========================')

print('Fim!')
