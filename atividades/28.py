# Apresentação
print('Programa para aplicar uma operação sobre 2 valores')
print()

# Entradas
v1 = float(input('Informe o primeiro valor: '))
v2 = float(input('Informe o segundo valor: '))

print()
print('Operações suportadas: ')
print('+  soma')
print('-  subtração')
print('*  multiplicação')
print('/  divisão')
print('** potenciação')
print()

op = input('Informe a operação desejada: ')

# Calcula o resultado e o apresenta na tela
print()
if (op == '+'):
    print(f'Resultado da operação: {v1 + v2}')
elif (op == '-'):
    print(f'Resultado da operação: {v1 - v2}')
elif (op == '*'):
    print(f'Resultado da operação: {v1 * v2}')
elif (op == '/'):
    print(f'Resultado da operação: {v1 / v2}')
elif (op == '**'):
    print(f'Resultado da operação: {v1 ** v2}')
else:
    print('Operação desconhecida: {op}')
