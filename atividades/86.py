# Apresentação
print('Programa para identificar quantas vezes um número X aparece em uma lista de valores')
print()

# Solicita os 10 valores
valores = [0] * 10

for i in range(len(valores)):
    valores[i] = int(input('Informe um número: '))

print()
valor_a_buscar = int(input('Informe o número a buscar na lista: '))

# Conta quantas vezes o número aparece na lista
qtde = 0
for v in valores:
    if (v == valor_a_buscar):
        qtde += 1

# Apresenta o resultado da contagem
print()
print(f'O número {valor_a_buscar} apareceu {qtde} vez(es) na lista de números informada.')
