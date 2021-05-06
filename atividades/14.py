# Apresentação
print('Programa para identificar se o índice de massa')
print('corporal está dentro dos parâmetros recomendados')
print('pela O.M.S')

# Entradas dos dados
peso = float(input('Informe o seu peso, em kg: '))
altura = float(input('Informe a sua altura, em metros: '))

# Processamento
imc = peso / (altura ** 2)

# Apresentar os resultados
print('O IMC dessa pessoa é:', imc)

if (imc >= 18.5 and imc <= 25):
    print('IMC dentro da faixa normal')
else:
    print('IMC fora da faixa normal')
