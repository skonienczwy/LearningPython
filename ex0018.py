print('##Exercicio 18##')

lado1 = float(input('Insira o primeiro valor: '))
lado2 = float(input('Insira o segundo valor: '))
lado3 = float(input('Insira o quarto valor: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com os segmentos acima pode-se formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('Equilatero')
    elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
        print('Isoceles')
    else:
        print('Escaleno')
else:
    print('Não se pode formar um triângulo')

