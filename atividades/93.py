# Apresentação
print('Programa para gerar a sequencia 0 0 1 1 um número determinado')
print('de vezes')
print()

# Quantidade de posições
qtde = int(input('Quantidade de posições: '))

# Vetor modelo, que será copiado até preencher o número de posiçõe
# desejadas
modelo = [0, 0, 1, 1]
# Posição a partir de onde será copiado o próximo elemento
posicao = 0

# Vetor que irá armazenar o resultado final
resultado = list()

for i in range(qtde):
    # Copiar o elemento indicado pela variável "posição" para o resultado
    resultado.append(modelo[posicao])

    # Atualiza a variável "posição" para a próxima iteração
    posicao += 1
    # Se ultrapassou a quantidade de posições disponíveis no modelo,
    # volta para o início
    if (posicao > len(modelo) - 1):
        posicao = 0

# Apresenta os valores na tela
print()
print('A lista de valores é: ')
for v in resultado:
    print(f'* {v}')
