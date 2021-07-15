# Apresentação
print('Programa para somar 8 valores utilizando vetores/listas')
print()

# Declaração do vetor
valores = [0, 0, 0, 0, 0, 0, 0, 0]

# Solicita os valores
for i in range(len(valores)):
    valores[i] = int(input('Informe o valor: '))

# Cálculo da soma
soma = 0
for i in range(len(valores)):
    soma += valores[i]

# Apresenta o resultado
print(f'A soma dos valores é {soma}')
