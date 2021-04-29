# Apresentação
print('Programa para calcular juros no regime de')
print('juros simples')
print()

# Entradas
c = float(input('Informe o capital: '))
i = float(input('Informe a taxa: '))
t = int(input('Informe o tempo: '))

# Processamento
resultado = c * (i / 100) * t

# Saídas
print('Os juros são de:', resultado)
