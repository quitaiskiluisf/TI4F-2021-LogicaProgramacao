# Apresentação
print('Programa para classificar pessoas de acordo com o sexo')
print()

# Declaração dos vetores para armazenar os dados
qtde_valores = 5
nomes = [''] * qtde_valores
sexos = [''] * qtde_valores

# Entrada dos dados
for i in range(qtde_valores):
    nomes[i] = input('Informe o nome da pessoa: ')
    sexos[i] = input('Informe o sexo da pessoa (M/F): ')
    print('-------------')

# Apresenta a lista das pessoas do sexo masculino
print()
print('Lista das pessoas do sexo masculino:')

for i in range(qtde_valores):
    if (sexos[i] == 'M'):
        print(f'* {nomes[i]}')

# Apresenta a lista das pessoas do sexo feminino
print()
print('Lista das pessoas do sexo feminino:')

for i in range(qtde_valores):
    if (sexos[i] == 'F'):
        print(f'* {nomes[i]}')
