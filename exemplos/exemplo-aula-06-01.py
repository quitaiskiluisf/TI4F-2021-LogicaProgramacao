def converte_fahrenheit_para_celsius(temperatura):
    return 5 * (temperatura - 32) / 9


# Apresentação
print('Programa para converter temperatura de °F para °C')
print()

# Entradas
f = float(input('Informe a temperatura 1, em °F: '))
f2 = float(input('Informe a temperatura 2, em °F: '))
f3 = float(input('Informe a temperatura 3, em °F: '))

# Processamento
c = converte_fahrenheit_para_celsius(temperatura=f)
c2 = converte_fahrenheit_para_celsius(temperatura=f2)
c3 = converte_fahrenheit_para_celsius(temperatura=f3)

# Saídas
print('A temperatura 1 em °C é', c)
print('A temperatura 2 em °C é', c2)
print('A temperatura 3 em °C é', c3)

