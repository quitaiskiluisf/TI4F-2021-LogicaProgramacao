# Apresentação
print('Programa para identificar se uma pessoa')
print('mora na região Sul')
print()

# Entradas
regiao_usuario = input('Em que estado você mora? ')

# Processamento e saídas
print()

estados_do_sul = ['RS', 'SC', 'PR']

if (regiao_usuario in estados_do_sul):
    print('Você mora na região Sul')
else:
    print('Você não mora na região Sul')
    print('O seu estado pertence à outra região')
