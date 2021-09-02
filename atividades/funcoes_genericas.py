def exemplo():
    ''' Função de exemplo '''
    print('Função de exemplo')


def exemplo2():
    print('Mensagem 2')


def exibe_matriz(mat):
    ''' Exibe a matriz na tela, reservando 15 espaços para cada valor '''
    for i in range(len(mat)): # Percorre todas as linhas da matriz
        for j in range(len(mat[i])): # Percorre todas as colunas
            print(f'{mat[i][j]:15}', end='')
        print()


def cria_matriz(linhas, colunas):
    ''' Cria uma matriz que possui a quantidade de linhas e colunas
        especificadas. O valor inicial de cada posição será 0. '''
    matriz = list()

    for i in range(linhas): # Faz a criação das linhas
        matriz.append([0] * colunas)
    
    return matriz
