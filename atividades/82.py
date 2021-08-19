# Apresentação do algoritmo
print('Programa para apresentar valores com um separador')
print()

# Declara o vetor com 11 posições e solicita os valores dele
valores = [0] * 11

for i in range(len(valores)):
    valores[i] = float(input('Informe um valor: '))

# Apresenta os valores, com um separador entre cada um
print()
print('Valores informados:')
for i in range(len(valores)):
    if (i != 0):
        print('-----------------')
    print(f'* {valores[i]}')
