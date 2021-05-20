def percentual_de_desconto(valor_da_compra):
    if (valor_da_compra >= 1500):
        return 15
    elif (valor_da_compra >= 750):
        return 12
    elif (valor_da_compra >= 250):
        return 7
    else:
        return 0


# Apresentação
print('Programa para cálculo do desconto em uma compra')
print()

# Entradas
valor_da_compra = float(input('Informe o valor da compra: '))

# Processamento
desconto = percentual_de_desconto(valor_da_compra=valor_da_compra)
valor_do_desconto = valor_da_compra * desconto / 100
valor_final = valor_da_compra - valor_do_desconto

# Saídas
print('Valor original da compra:', valor_da_compra)
print('Desconto recebido       :', valor_do_desconto, ' (', desconto, '%)')
print('Valor final             :', valor_final)
