# Apresentação
print('Programa para calcular a área de vários retângulos')
print()

tem_proximo_retangulo = 'S'

while (tem_proximo_retangulo == 'S'):
    # Solicita os dados e faz o cálculo
    base = float(input('Informe a medida da base: '))
    altura = float(input('Informe a medida da altura: '))

    resultado = base * altura

    # Mostra os dados
    print(f'A área desse retângulo é: {resultado:.3f}')

    print()
    tem_proximo_retangulo = input('Deseja calcular a área de mais um retângulo. Informe "S" para "Sim": ')

print('Obrigado por executar este programa.')
