# Apresentação
print('Programa para somar os números inteiros')
print('existentes entre 1 e 10.000')
print()

# Laço que vai de 1 até 10.000
soma = 0
for i in range(1, 10001):
    soma = soma + i

print('O somatório é', soma)
