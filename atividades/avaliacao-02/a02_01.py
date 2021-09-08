# Apresentação
print('Programa para fazer operações com vetores')
print()

# Solicita os 10 valores
valores = list()

for i in range(10):
    valores.append(int(input('Informe um número inteiro: ')))

# Multiplica o valor das posições pares por -2
for i in range(0, len(valores), 2):
    valores[i] *= -2

# Soma 10000 ao valor das posições ímpares
for i in range(1, len(valores), 2):
    valores[i] += 10000

# Apresenta os valores na tela
print()
for valor in valores:
    print(valor)
