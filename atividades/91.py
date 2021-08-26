# Apresentação
print('Programa para solicitar 2 vetores e somar eles de forma cruzada')
print()

# Declara e solicita os dados do 1º vetor
v1 = list()
print('Valores que irão compor o 1º vetor')
for i in range(17):
    valor = int(input('Informe um valor: '))
    v1.append(valor)
print()

# Declara e solicita os dados do 2º vetor
v2 = list()
print('Valores que irão compor o 2º vetor')
for i in range(17):
    valor = int(input('Informe um valor: '))
    v2.append(valor)
print()

# Declara o vetor que conterá os resultados
v3 = list()

# Posição correspondente em B. Inicia ela com a última posição do vetor
j = len(v2) - 1

# Percorre todas as posições de A
for i in range(len(v1)):
    # Faz a soma de 1 posição de v1 com uma de v2, e armazena em v3
    v3.append(v1[i] + v2[j])

    # Atualiza a variável de controle j
    j -= 1

# Apresenta os valores na tela
print()
print('Valores resultantes')
for v in v3:
    print(f'* {v}')
