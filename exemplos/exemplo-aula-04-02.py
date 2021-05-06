# Apresentação
print('Programa para calcular o peso ideal de uma pessoa')
print()

# Entradas
altura = float(input('Informe a sua altura, em metros: '))
sexo = input('Informe o seu sexo (M/F): ')

# Processamento e saídas
if (sexo == 'M' or sexo == 'm'):
    peso_ideal = 72.7 * altura - 58
    print('O peso ideal é', peso_ideal)
elif (sexo == 'F' or sexo == 'f'):
    peso_ideal = 62.1 * altura - 44.7
    print('O peso ideal é', peso_ideal)
else:
    print('O sexo informado é inválido')
