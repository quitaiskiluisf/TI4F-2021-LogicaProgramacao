# Apresentação
print('Programa para ordenar um vetor de inteiros maiores que 0')
print()

# Solicita os 15 valores
valores = list()

while (len(valores) < 15):
    valor_informado = int(input('Informe um valor: '))

    # Rejeita o valor 0 e inferiores à ele
    if (valor_informado <= 0):
        print('O valor informado é inválido. Informe outro')
        print()
    else:
        valores.append(valor_informado)

# Ordena os valores
valores.sort()

# Apresenta os valores na tela, em uma mesma linha, separados por espaço
for v in valores:
    print(v, end='  ')

print()
