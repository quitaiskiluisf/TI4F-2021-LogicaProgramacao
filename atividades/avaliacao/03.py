def awg_para_mm(n_awg):
    ''' Converte uma medida de AWG para o equivalente em mm. '''
    return 0.127 * 92 ** ((36 - n_awg) / 39)


# Apresentação
print('Programa para converter a especificação em AWG de um cabo')
print('para o diâmetro em mm.')
print()

# Entradas
awg = int(input('Informe a especificação do cabo em AWG: '))

# Processamento
print()
if (awg >= 0 and awg <= 40):
    mm = awg_para_mm(n_awg=awg)

    # Saídas
    print(f'A medida em milímetros é: {mm:.2f}')
else:
    print('O valor especificado é inválido.')
