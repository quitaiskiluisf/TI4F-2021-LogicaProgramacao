# Apresentação
print('Programa para calcular estatísticas dos números e um vetor')
print()

# Solicita os 18 valores
valores = list()
for i in range(18):
    valores.append(float(input('Informe um número: ')))

# Calcula a média dos valores (somatório de todos os
# valores dividido pela quantidade de valores existentes)
media = sum(valores) / len(valores)

# Calcula a amplitude (diferença entre o maior valor e
# o menor valor existentes no vetor)
amplitude = max(valores) - min(valores)

# Apresenta os resultados
print()
print(f'A média dos valores informados é {media}')
print(f'A amplitude dos valores informados é {amplitude}')
