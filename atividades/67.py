# Apresentação
print('Programa para calcular fatorial utilizando laços de repetição')
print()

# Entradas
valor = int(input('Informe o valor desejado: '))

# Processamento e saídas
if (valor >= 0):
    # Calcula o fatorial
    resultado = 1
    for i in range(2, valor + 1):
        resultado *= i

    # Apresenta o resultado
    print()
    print(f'O resultado é: {resultado}')
else:
    # Mensagem para caso o usuário informou um número negativo
    print('Números negativos não possuem fatorial')
