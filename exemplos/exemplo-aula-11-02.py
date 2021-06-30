# Apresentação
print('Programa para somar 10 valores')
print()

# Variável que irá armazenar o valor da soma dos valores
# informados pelo usuário
soma = 0

# Solicita o valor e o adiciona na variável soma
for i in range(10):
    soma = soma + int(input('Informe um valor: '))

# Apresenta o somatório
print('A soma dos valores é', soma)

