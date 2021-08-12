# Apresentação
print('Programa para solicitar valores, armazená-los')
print('em um vetor e fazer algumas operações.')
print()

# Declaração do vetor
valores = [0] * 7

# Solicitar os valores para o usuário
for i in range(len(valores)):
    valor = float(input('Informe um valor: '))
    valores[i] = valor

# Cálculo da média
soma = 0
for i in range(len(valores)):
    soma += valores[i]
media = soma / len(valores)

print(f'O valor da média é: {media}')

# Altera os valores menores que a média para zero
for i in range(len(valores)):
    if valores[i] <= media:
        valores[i] = 0

# Apresenta os valores do vetor na tela
for i in range(len(valores)):
    print(f'{valores[i]}')
