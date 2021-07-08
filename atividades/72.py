# Apresentação
print('Programa para calcular a média de 12 valores')
print()

# Variável para controlar quantas vezes o laço já executou
i = 0
soma = 0
while (i < 12):
    # Solicita um valor e adiciona ele na variável que tem
    # a soma
    soma += float(input('Informe um valor: '))

    # Atualizar a variável de controle
    i += 1

# Calcula a média e apresenta na tela
resultado = soma / 12
print(f'A média dos valores informados é: {resultado:.3f}')
