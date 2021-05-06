# Apresentação
print('Programa para identificar a que cargos eletivos')
print('uma pessoa pode se candidatar com base em sua idade')
print()

# Entradas
idade = int(input('Informe a sua idade: '))

# Processamento e saídas

print('Esta pessoa pode se candidatar a estes cargos:')

if (idade < 18):
    print('- Nenhum cargo disponível')

if (idade >= 18):
    print('- Vereador')

if (idade >= 21):
    print('- Deputado Federal')
    print('- Deputado Estadual ou Distrital')
    print('- Prefeito ou Vice-Prefeito')
    print('- Juiz de paz')

if (idade >= 30):
    print('- Governador ou Vice-Governador')

if (idade >= 35):
    print('- Presidente ou Vice-Presidente')
    print('- Senador')
