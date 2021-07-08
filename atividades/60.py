def celsius_para_fahrenheit(tc):
    ''' Converte graus Celsius para graus Fahrenheit '''
    return (9 * tc + 160) / 5


# Apresentação
print('Programa para mostrar a tabela de conversão')
print('de graus Celsius para graus Fahrenheit')
print()

for i in range(-10, 51, 2):
    # Cálculo da temperatura em graus Fahrenheit
    f = celsius_para_fahrenheit(tc=i)
    print(f'{i:4}°C = {f}°F')
