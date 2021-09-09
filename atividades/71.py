def eh_bissexto(ano):
    ''' Determina se o ano informado é bissexto. '''
    d4 = (ano % 4) == 0
    d100 = (ano % 100) == 0
    d400 = (ano % 400) == 0
    return (d4 and d100 and d400) or (d4 and not d100)


def qtde_dias_mes(mes, ano):
    ''' Retorna a quantidade de dias que um determinado mês possui.
        Mês é um número inteiro: 1 - Jan, 2 - Fev, ..., 12 - Dezembro'''
    if (mes in [1, 3, 5, 7, 8, 10, 12]):
        return 31
    if (mes in [4, 6, 9, 11]):
        return 30
    if (mes == 2):
        if (eh_bissexto(ano)):
            return 29
        else:
            return 28
    else:
        return 0


# Apresentação
print('Programa para acrescentar um intervalo em uma data')
print()

# Entradas
print('DATA INICIAL')
dia = int(input('Informe o dia (apenas números): '))
mes = int(input('Informe o mês (apenas números): '))
ano = int(input('Informe o ano (apenas números): '))
print()
print('INTERVALO')
intervalo = int(input('Em quantos dias gostaria de avançar a data (apenas números)? '))

if (mes >= 1 and mes <= 12): # Valida o mês
    if (dia <= qtde_dias_mes(mes, ano)): # Valida o dia
        if (intervalo >= 0): # Valida o intervalo
            # Executa o laço de repetição uma vez para cada dia a avançar
            for i in range(intervalo):
                dia += 1

                # Se o número de dias avançou o máximo, reseta ele para 1 e aumenta os meses
                if (dia > qtde_dias_mes(mes, ano)):
                    dia = 1
                    mes += 1

                # Se o número de meses avançou o máximo, reseta ele para 1 e aumenta o ano
                if (mes > 12):
                    mes = 1
                    ano += 1

            # Apresenta a data final
            print()
            print('DATA AVANÇADA')
            print(f'Nova data = {dia}/{mes}/{ano}')
        else:
            print('O intervalo deve ser um número inteiro positivo')
    else:
        print('O número de dias informado é inválido para mês escolhido')
else:
    print('O mês informado é inválido')
