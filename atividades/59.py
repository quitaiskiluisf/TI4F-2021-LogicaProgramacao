import math

# Apresentação
print('Programa para calcular a área de múltiplos círculos')
print()

# Solicita a quantidade de círculos desejados
qtde = int(input('De quantos círculos deseja calcular a área? '))

for i in range(1, qtde + 1):
    # Separador
    print(f'====== DADOS DO CÍRCULO {i} ======')

    # Solicita os dados
    raio = float(input('Informe o valor do raio: '))

    # Cálculo
    resultado = math.pi * raio ** 2

    # Exibe o resultado
    print(f'A área do círculo é {resultado:.4f}')
