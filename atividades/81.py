# Construa um algoritmo que solicite números inteiros para o usuário. Ele deve
# seguir solicitando números até o usuário informar o valor 0. Ao final, apresente:
# a. O maior valor informado
# b. O menor valor informado
# c. A quantidade total de valores informados
# d. A quantidade de valores positivos informados;
# e. A quantidade de valores negativos informados.

# Apresentação
print('Programa para solicitar valores inteiros e calcular algumas estatísticas')
print('considerando os valores informados')
print()

# Variáveis que armazenarão as estatísticas
o_maior = 0
o_menor = 0
qtde = 0
qtde_positivo = 0
qtde_negativo = 0

# Variável que armazena o valor que o usuário nos informar
n = -1

while (n != 0):
    # Solicita o valor para o usuário
    n = int(input('Informe um valor: '))

    # Quando o usuário informar 0, mostra as estatísticas na tela
    # Quando informar outro valor, atualiza as variáveis com as estatísticas
    if (n != 0):
        # Atualiza a quantidade geral
        qtde += 1

        # Atualiza a quantidade de valores positivos
        if (n > 0):
            qtde_positivo += 1

        # Atualiza a quantidade de valores negativos
        if (n < 0):
            qtde_negativo += 1

        # Atualiza o menor e o maior valor que o usuário já informou
        # Mas, na primeira execução, atribuir à elas o próprio valor que o usuário
        # informou
        if (qtde == 1):
            o_maior = n
            o_menor = n
        else:
            # Atualiza o maior valor, se necessário
            if (n > o_maior):
                o_maior = n

            # Atualiza o menor valor, se necessário
            if (n < o_menor):
                o_menor = n
    else:
        # Apresenta as estatísticas, se foi informado algum valor
        if (qtde > 0):
            print(f'O maior valor informado foi: {o_maior}')
            print(f'O menor valor informado foi: {o_menor}')
            print(f'A quantidade total de valores informados foi: {qtde}')
            print(f'A quantidade de valores positivos foi: {qtde_positivo}')
            print(f'A quantidade de valores negativos foi: {qtde_negativo}')
        else:
            print('Não foi informado nenhum valor.')
