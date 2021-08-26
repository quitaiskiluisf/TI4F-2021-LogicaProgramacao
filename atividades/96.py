# Apresentação
print('Programa para identificar valores comuns em 2 listas')
print()

# Vetor 1: declara e solicita os valores
v1 = list()
print('Dados referentes à lista 1')
for i in range(10):
    valor = input('Informe um valor: ')
    v1.append(valor)
print()

# Vetor 2: declara e solicita os valores
v2 = list()
print('Dados referentes à lista 2:')
for i in range(12):
    valor = input('Informe um valor: ')
    v2.append(valor)
print()

# Vetor com os resultados: contém os números comuns às duas listas
comuns = list()

# Percorre os elementos da 1ª lista e testa se ele existe na 2ª;
# Se existe, esse elemento será acrescentado na lista "comuns"
for elemento in v1:
    if elemento in v2:
        comuns.append(elemento)

# Ordena os valores comuns em ordem decrescente
comuns.sort(reverse=True)

# Exibe os valores comuns na tela
print('Valores comuns às duas listas:')
for valor in comuns:
    print(f'* {valor}')
