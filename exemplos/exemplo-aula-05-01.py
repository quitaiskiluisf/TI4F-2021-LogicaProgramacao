# Apresentação
print('Programa para determinar o desconto')
print()

# Entradas
valor_compra = float(input('Informe o valor da compra: '))

# Processamento

# Determina qual é o desconto
desconto = 0
if (valor_compra >= 1500):
    desconto = 15
elif (valor_compra >= 750):
    desconto = 12
elif (valor_compra >= 250):
    desconto = 7

# Calcula o desconto, em R$
desconto_reais = valor_compra * desconto / 100
# Calcula o valor final
valor_final = valor_compra - desconto_reais

# Saídas
print('Recebeu', desconto, '% de desconto')
print('Desconto em R$:', desconto_reais)
print('Valor final   :', valor_final)
