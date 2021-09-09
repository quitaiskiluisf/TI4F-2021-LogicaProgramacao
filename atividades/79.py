# Apresentação
print('Programa para calcular o resultado do somatório dos 30 primeiros termos da série')
print('x/1 + x/2 + x/3 + ... + x/29 + x/30')
print()

# Entradas
x = float(input('Informe o valor para o termo X: '))

# Processamento
i = 1
resultado = 0
while (i <= 30):
    resultado += x / i
    i += 1

# Saídas
print()
print(f'O somatório dos termos da série é {resultado}')
