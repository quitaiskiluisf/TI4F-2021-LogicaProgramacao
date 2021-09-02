from funcoes_genericas import exibe_matriz, cria_matriz

# Apresentação
print('Programa para calcular o determinante de uma matriz de 2 x 2')
print()

# Declaração da matriz
matriz = cria_matriz(linhas=2, colunas=2)

# Solicita os valores para o usuário
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = float(input(f'Informe o valor para a posição [{i + 1}, {j + 1}]: '))

# Apresenta a matriz
print()
print('Matriz informada: ')
exibe_matriz(mat=matriz)

# Faz o cálculo
det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

# Apresenta o resultado
print()
print(f'O determinante é: {det:.2f}')
