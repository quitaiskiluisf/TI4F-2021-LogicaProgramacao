# Apresentação
print('Programa para apurar o resultado de um aluno')
print()

# Entradas
n1 = float(input('Informe a nota 1 do aluno: '))
n2 = float(input('Informa a nota 2 do aluno: '))

# Processamento
media = (n1 + n2) / 2

# Saídas
print('Média do aluno: ', media)

if (media >= 6):
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
