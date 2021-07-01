def diaria_cama_casal(n_camas):
    ''' O quanto as camas de casal contribuem para a diária. '''
    if (n_camas == 1):
        return 140
    else:
        return 0


def diaria_cama_solteiro(n_camas):
    ''' O quanto as camas de solteiro contribuem para a diária. '''
    if (n_camas == 1):
        return 90
    elif (n_camas == 2):
        return 155
    elif (n_camas == 3):
        return 215
    else:
        return 0


# Apresentação
print('Programa para calcular o valor a pagar')
print('em uma pousada')
print()

# Entradas
n_dias = int(input('Informe a quantidade de dias: '))
camas_solteiro = int(input('Informe a quantidade de camas de solteiro desejadas: '))
camas_casal = int(input('Informe a quantidade de camas de casal desejadas: '))
ar_condicionado = input('Deseja ar condicionado (Sim/Não)? ')

# Processamento
diaria = diaria_cama_casal(n_camas=camas_casal) + diaria_cama_solteiro(n_camas=camas_solteiro)

if (camas_solteiro in [0, 1, 2, 3]):
    if (camas_casal in [0, 1]):
        if ((camas_solteiro + camas_casal) >= 1):
            # Optou pelo ar condicionado? Se sim, acrescenta o valor na diária
            if (ar_condicionado.upper() == "SIM"):
                diaria = diaria + 20
            
            # Calcula o valor final de acordo com o  número de dias escolhido
            valor_final = diaria * n_dias

            # Apresentação dos resultados
            print(f'Valor final da reserva: R$ {valor_final:.2f}')
        else:
            print('Deve-se escolher pelo menos 1 cama')
    else:
        print('Opção inválida de número de camas de casal.')
else:
    print('Opção inválida de número de camas de solteiro.')