# Apresentação
print('Programa para somar 10 valores')
print()

# Variável de controle
i = 0

# Variável que conterá o somatório total dos valores
soma = 0

while (i < 10):
    soma += int(input('Informe um valor: '))

    i += 1

# Saídas
print(f'A soma é: {soma}')
