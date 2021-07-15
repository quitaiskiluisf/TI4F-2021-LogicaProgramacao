def eh_maior_de_idade(idade):
    ''' Determina se uma pessoa é maior de idade '''
    return (idade >= 18)


# Apresentação
print('Programa para verificar se uma pessoa')
print('é maior de idade')
print()

# Entradas
nome = input('Informe o nome da pessoa: ')
idade = int(input('Informe a idade da pessoa: '))

# Processamento e saídas
print()
if (eh_maior_de_idade(idade)):
    print(f'O(a) "{nome}" é maior de idade')
else:
    print(f'O(a) "{nome}" NÃO é maior de idade')
