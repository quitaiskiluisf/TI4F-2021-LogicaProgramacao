# Apresentação
print('Programa para solicitar 12 valores e separar os pares dos ímpares')
print()

# Declaração do vetor e solicitação dos valores
valores = [0] * 12

for i in range(len(valores)):
    valores[i] = int(input('Informe um valor: '))

# Apresenta os valores pares
print()
print('Números pares:')
for i in range(len(valores)):
    if (valores[i] % 2 == 0):
        print(f'* {valores[i]}')

# Apresenta os valores ímpares
print()
print('Números ímpares:')
for i in range(len(valores)):
    if (valores[i] % 2 != 0):
        print(f'* {valores[i]}')
