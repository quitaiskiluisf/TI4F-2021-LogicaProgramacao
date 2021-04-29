# Apresentação
print('Programa para analisar a velocidade média')
print()

# Entradas
km_percorridos = float(input('Informe a distância percorrida, em km: '))
tempo = float(input('Informe a duração da viagem, em horas: '))

# Processamento
velocidade_media = km_percorridos / tempo

# Saídas
print('Velocidade média = ', velocidade_media)

if (velocidade_media >= 90):
    print('Motorista dirige muito rápido')
else:
    print('Motorista dirige dentro do limite')
