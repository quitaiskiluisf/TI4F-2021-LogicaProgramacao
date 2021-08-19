# Apresentação
print('Programa para solicitar 18 valores e exibí-los na ordem contrária')
print()

# Declaração do vetor e solicitação dos valores para o usuário
valores = [0] * 18

for i in range(len(valores)): # 0, 1, 2, 3, 4, ..., 16, 17
    valores[i] = int(input('Informe um valor: '))

# Exibe os valores, de trás para frente
print()
print('Valores informados, em ordem inversa:')
for i in range(len(valores) - 1, -1, -1): # 17, 16, 15, ..., 3, 2, 1, 0
    print(f'* {valores[i]}')
