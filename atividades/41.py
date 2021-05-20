def inverso(numero):
    return 1 / numero


# Apresentação
print('Programa para calcular o inverso de alguns números')
print()

# Entradas
v1 = float(input('Informe o valor 1: '))
v2 = float(input('Informe o valor 2: '))
v3 = float(input('Informe o valor 3: '))
v4 = float(input('Informe o valor 4: '))

# Processamento
resultado1 = inverso(numero=v1)
resultado2 = inverso(numero=v2)
resultado3 = inverso(numero=v3)
resultado4 = inverso(numero=v4)

# Saídas
print()
print('Inverso do 1° valor:', resultado1)
print('Inverso do 2° valor:', resultado2)
print('Inverso do 3° valor:', resultado3)
print('Inverso do 4° valor:', resultado4)
