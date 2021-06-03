def retorna_regiao(estado):
    ''' Retorna o nome da região à qual um
        estado brasileiro pertence.

        O parâmetro "estado" deve ser a sigla
        do estado desejado. '''
    # Converte a sigla do estado para letras maiúsculas.
    estado = estado.upper()

    if (estado in ['PR', 'RS', 'SC']):
        return 'Sul'
    elif (estado in ['ES', 'MG', 'RJ', 'SP']):
        return 'Sudeste'
    elif (estado in ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']):
        return 'Norte'
    elif (estado in ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']):
        return 'Nordeste'
    elif (estado in ['DF', 'GO', 'MT', 'MS']):
        return 'Centro-Oeste'
    else:
        return ''


def retorna_capital(estado):
    ''' Retorna o nome da capital de um estado
        brasileiro.

        O parâmetro "estado" deve ser a sigla
        do estado desejado. '''
    # Converte a sigla do estado para letras maiúsculas.
    estado = estado.upper()

    if (estado == 'PR'):
        return 'Curitiba'
    elif (estado == 'RS'):
        return 'Porto Alegre'
    elif (estado == 'SC'):
        return 'Florianópolis'
    elif (estado == 'ES'):
        return 'Vitória'
    elif (estado == 'MG'):
        return 'Belo Horizonte'
    elif (estado == 'RJ'):
        return 'Rio de Janeiro'
    elif (estado == 'SP'):
        return 'São Paulo'
    elif (estado == 'AC'):
        return 'Rio Branco'
    elif (estado == 'AP'):
        return 'Macapá'
    elif (estado == 'AM'):
        return 'Manaus'
    elif (estado == 'PA'):
        return 'Belém'
    elif (estado == 'RO'):
        return 'Porto Velho'
    elif (estado == 'RR'):
        return 'Boa Vista'
    elif (estado == 'TO'):
        return 'Palmas'
    elif (estado == 'AL'):
        return 'Maceió'
    elif (estado == 'BA'):
        return 'Salvador'
    elif (estado == 'CE'):
        return 'Fortaleza'
    elif (estado == 'MA'):
        return 'São Luís'
    elif (estado == 'PB'):
        return 'João Pessoa'
    elif (estado == 'PE'):
        return 'Recife'
    elif (estado == 'PI'):
        return 'Teresina'
    elif (estado == 'RN'):
        return 'Natal'
    elif (estado == 'SE'):
        return 'Aracaju'
    elif (estado == 'DF'):
        return 'Brasília'
    elif (estado == 'GO'):
        return 'Goiânia'
    elif (estado == 'MT'):
        return 'Cuiabá'
    elif (estado == 'MS'):
        return 'Campo Grande'
    else:
        return ''


# Apresentação
print('Programa para determinar a capital e a região à que um estado pertence')
print()

# Entradas
estado = input('Informe a sigla do estado: ')

# Processamento
nome_regiao = retorna_regiao(estado=estado)
nome_capital = retorna_capital(estado=estado)

# Saídas
print('Região  =', nome_regiao)
print('Capital =', nome_capital)
