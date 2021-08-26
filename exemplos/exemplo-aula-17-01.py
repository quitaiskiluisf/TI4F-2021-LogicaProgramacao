# Apresentação
print('Programa para solicitar 12 valores e multiplicá-los por 2.8')
print()

# Declara o vetor e solicita o valor das posições
valores = list()

for i in range(12):
    valor = float(input('Informe um valor: '))
    valores.append(valor)

# Multiplica cada posição do vetor por 2.8
for i in range(len(valores)):
    valores[i] *= 2.8

# Apresenta os resultados finais
print()
for v in valores:
    print(f'* {v:.2f}')
