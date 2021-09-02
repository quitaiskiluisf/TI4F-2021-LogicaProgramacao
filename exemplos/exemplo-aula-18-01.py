def exibe_matriz(mat):
    ''' Exibe a matriz na tela, reservando 15 espaços para cada valor '''
    for i in range(len(mat)): # Percorre todas as linhas da matriz
        for j in range(len(mat[i])): # Percorre todas as colunas
            print(f'{mat[i][j]:15}', end='')
        print()


# Apresentação
print('Programa para multiplicar uma matriz por uma constante')
print()

# Declara a matriz
mat = list()
for i in range(3): # Esta parte define a qtde de linhas da matriz
    mat.append([0] * 4) # Esta parte define a qtde de colunas da matriz

# Solicita os valores para o usuário
for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] = float(input(f'Informe um valor para a posição [{i + 1}, {j + 1}]: '))

# Apresenta a matriz informada
print()
print('Valores informados: ')
exibe_matriz(mat=mat)

# Solicita a constante
print()
c = float(input('Informe a constante para multiplicar os valores: '))

# Faz o cálculo
for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] *= c  # Equivalente à mat[i][j] = mat[i][j] * c

# Exibe o resultado
print()
print('Matriz multiplicada: ')
exibe_matriz(mat=mat)
