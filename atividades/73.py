# Apresentação
print('Programa para somar os valores entre 1 e 10.000')
print()

# Variável de controle
numero = 1

# Armazena o resultado do cálculo
soma = 0

# Criação do laço que irá executar 10.000 vezes
while (numero <= 10000):
    soma += numero

    # Atualiza a variável de controle
    numero += 1

# Resultados
print(f'O somatório dos valores é: {soma}')
