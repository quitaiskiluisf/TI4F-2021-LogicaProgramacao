# Apresentação
print('Programa para converter velocidade')
print('de knots para km/h e mi/h')

# Entradas
knots = float(input('Informe a velocidade em knots: '))

# Processamento
velocidade_kmh = knots * 1.852
velocidade_mih = knots * 1.1508

# Saída
print('Velocidade em km/h:', velocidade_kmh)
print('Velocidade em mi/h:', velocidade_mih)
