# Apresentação
print('Programa para verificar se a pessoa já pode fazer')
print('a sua CNH.')

# Variável que irá armazenar a idade da pessoa
# Inicio ela com um valor inválido para que o laço de repetição
# execute pelo menos uma vez.
idade = -1

while (idade < 0 or idade > 120):
    idade = int(input('Informe a sua idade: '))

    if (idade < 0 or idade > 120):
        print('Idade inválida. Tente novamente.')

if (idade >= 18):
    print('A pessoa já pode fazer a sua CNH.')
else:
    print('A pessoa inda não pode fazer a sua CNH.')
