def geracao(ano):
    ''' Determina a que geração uma pessoa nascida
        no ano fornecido pertence. '''
    if (ano < 1940):
        return 'Geração sem classificação'
    elif (ano >= 1940 and ano <= 1959):
        return 'Geração Baby Boomer'
    elif (ano >= 1960 and ano <= 1979):
        return 'Geração X'
    elif (ano >= 1980 and ano <= 1994):
        return 'Geração Y'
    elif (ano >= 1995 and ano <= 2009):
        return 'Geração Z'
    else:
        return 'Geração Alpha'


# Apresentação
print('Programa para calcular a geração a que')
print('duas pessoas pertencem')
print()

# Entradas
ano1 = int(input('Informe o ano de nascimento da pessoa 1: '))
ano2 = int(input('Informe o ano de nascimento da pessoa 2: '))

# Processamento
geracao1 = geracao(ano=ano1)
geracao2 = geracao(ano=ano2)

# Saídas
print()
print(f'A pessoa 1 pertence à {geracao1}.')
print(f'A pessoa 2 pertence à {geracao2}.')
