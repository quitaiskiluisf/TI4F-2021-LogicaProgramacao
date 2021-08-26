# Apresentação
print('Programa para solicitar valores únicos e ordená-los')
print()

# Declara o vetor e solicita os valores
valores = list()

while (len(valores) < 16):
    # Solicita um valor
    valor_temporario = int(input('Informe um número inteiro: '))

    # Verifica se o valor já existe na lista; se não existe, adiciona;
    # se existe, mostra um erro e o laço irá solicitar um novo
    if (valor_temporario in valores):
        print('Este valor já existe. Informe outro.')
        print()
    else:
        valores.append(valor_temporario)

# Ordena a lista de valores
valores.sort()

# Mostra a lista de valores na tela
print()
for v in valores:
    print(f'* {v}')
