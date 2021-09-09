# Apresentação
print('Programa para calcular o conceito de um aluno, com base na média de 3 notas')
print()

# Solicita as 3 notas
n1 = float(input('Informe a nota 01: '))
n2 = float(input('Informe a nota 02: '))
n3 = float(input('Informe a nota 03: '))

# Calcula e apresenta a média
print()
media = (n1 + n2 + n3) / 3
print(f'Média das notas = {media}')

# Apresenta o conceito correspondente
if (media >= 9):
    print('Conceito = A')
elif (media >= 7.5):
    print('Conceito = B')
elif (media >= 6):
    print('Conceito = C')
elif (media >= 4):
    print('Conceito = D')
else:
    print('Conceito = E')
