# Apresentação
print('Programa para determinar se o custo do envio de um produto')
print('será feito considerando-se o peso físico ou o peso cúbico')
print()

# Entradas
print('Informações sobre o pacote')
altura = float(input('Informe a altura (em cm): '))
largura = float(input('Informe a largura (em cm): '))
comprimento = float(input('Informe o comprimento (em cm): '))
peso_fisico = float(input('Informe o peso físico (em kg): '))

# Processamento e saídas
print()
peso_cubico = altura * largura * comprimento / 6000
print(f'Peso cúbico do pacote: {peso_cubico}kg')
print()

if (peso_cubico > peso_fisico):
    print('O frete será calculado considerando-se o PESO CÚBICO do pacote')
else:
    print('O frete será calculado considerando-se o PESO FÍSICO do pacote')
