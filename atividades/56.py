# Apresentação
print('Programa para calcular a média de 12 valores')
print()

soma = 0
for i in range(12):
    soma = soma + float(input('Informe um valor: '))

media = soma / 12

print('A média é', media)
