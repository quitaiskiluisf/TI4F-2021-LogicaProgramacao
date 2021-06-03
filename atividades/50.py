def ipva_estado(estado):
    ''' Retorna o percentual cobrado
        de IPVA para um veículo.

        O parâmetro "estado" é a sigla
        do estado desejado. '''
    # Converte a sigla do estado para maiúsculo
    estado = estado.upper()

    if (estado == 'ES'):
        return 1.0
    elif (estado in ['AC', 'AM', 'MT', 'RO', 'SC']):
        return 2.0
    elif (estado in ['BA', 'CE', 'MA', 'PA', 'PB', 'PI', 'SR', 'TO']):
        return 2.5
    elif (estado == 'AL'):
        return 2.75
    elif (estado in ['AP', 'PE', 'RN', 'RS', 'RR']):
        return 3.0
    elif (estado in ['DF', 'MS', 'PR', ]):
        return 3.5
    elif (estado == 'GO'):
        return 3.75
    elif (estado in ['MG', 'RJ', 'SP']):
        return 4.0
    else:
        return 0.0


# Apresentação
print('Programa para estimar o valor do IPVA para um veículo')
print()

# Entradas
estado = input('Informe a sigla do estado onde o veículo está registrado: ')
valor_veiculo = float(input('Informe o valor do veículo: '))

# Processamento
percentual_ipva = ipva_estado(estado=estado)
valor_ipva = valor_veiculo * percentual_ipva / 100

# Saídas
print('Percentual de imposto: ', percentual_ipva, '%')
print('Valor aproximado do imposto: R$', valor_ipva)
