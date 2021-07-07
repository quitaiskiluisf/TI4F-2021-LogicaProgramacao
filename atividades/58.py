# Apresentação
print('Programa para apresentar a tabuada de um número')
print()

# Solicita a tabuada desejada
tabuada = int(input('De que número deseja ver a tabuada? '))

for i in range(11):
    # Calcula o valor da multiplicação para exibir na tela
    resultado = tabuada * i

    print(f'{tabuada} x {i:2} = {resultado}')
