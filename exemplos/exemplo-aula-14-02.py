# Apresentação
print('Programa para solicitar números e classificá-los')
print()

# Declaração do vetor com 10 posições
valores = [0] * 10

# Solicita os valores para o usuário
for i in range(len(valores)):
    valores[i] = int(input('Informe um valor: '))

# Cálculo da média
soma = 0
for i in range(len(valores)):
    soma += valores[i]

media = soma / len(valores)

print()
print(f'A média dos valores é: {media}')

# Apresenta a lista dos valores menores que a média
print()
print('Valores menores que a média: ')

for i in range(len(valores)):
    if (valores[i] < media):
        print(f'* {valores[i]}')


# Apresenta a lista dos valores maiores que a média
print()
print('Valores maiores que a média: ')

for i in range(len(valores)):
    if (valores[i] > media):
        print(f'* {valores[i]}')
