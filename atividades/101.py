from funcoes_genericas import exibe_matriz, cria_matriz

# Apresentação
print('Programa para somar 2 matrizes de 4 x 3')
print()

# Declaração das matrizes
m1 = cria_matriz(linhas=4, colunas=3)
m2 = cria_matriz(linhas=4, colunas=3)
mr = cria_matriz(linhas=4, colunas=3)

# Solicita os valores - Matriz 1
print('Matriz 1:')
for i in range(len(m1)):
    for j in range(len(m1[i])):
        m1[i][j] = float(input(f'Informe um valor para a posição [{i + 1}, {j + 1}]: '))

# Solicita os valores - Matriz 2
print()
print('Matriz 2:')
for i in range(len(m2)):
    for j in range(len(m2[i])):
        m2[i][j] = float(input(f'Informe um valor para a posição [{i + 1}, {j + 1}]: '))

# Apresenta as 2 matrizes:
print()
print('Matriz 1: ')
exibe_matriz(mat=m1)
print()
print('Matriz 2:')
exibe_matriz(mat=m2)

# Faz o cálculo
for i in range(len(mr)):
    for j in range(len(mr[i])):
        mr[i][j] = m1[i][j] + m2[i][j]

# Apresenta a matriz final
print()
print('Resultado da soma:')
exibe_matriz(mat=mr)
