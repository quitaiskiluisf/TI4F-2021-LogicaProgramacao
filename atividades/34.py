# Apresentação
print('Programa para identificar se 3 medidas permitem formar um triângulo')
print('Se formam, determina também qual o tipo de triângulo formado')
print()

# Entradas
lado_a = float(input('Informe a medida do lado A: '))
lado_b = float(input('Informe a medida do lado B: '))
lado_c = float(input('Informe a medida do lado C: '))

# Processamento e saídas
print()
if (((lado_a + lado_b) > lado_c) and ((lado_b + lado_c) > lado_a) and ((lado_a + lado_c) > lado_b)): # Testa se forma um triângulo
    # Testa se todos lados são iguais
    if ((lado_a == lado_b) and (lado_b == lado_c)):
        print('Forma um triângulo equilátero')
    # Testa se existem 2 iguais
    elif ((lado_a == lado_b) or (lado_b == lado_c) or (lado_a == lado_c)):
        print('Forma um triângulo isósceles')
    # Forma triângulo, mas não é equilátero e nem isósceles
    else:
        print('Forma um triângulo escaleno')
else:
    print('As medidas informadas não permitem formar um triângulo')
