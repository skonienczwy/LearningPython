print('##Exercicio 14##')

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if val1 > val2:
    print(f'Valor {val1} é maior do que {val2} - Primeiro valor digitado')
elif val2 > val1:
    print(f'Valor {val2} é maior do que {val1} - Segundo valor digitado')
else:
    print(f'Os valores {val1} e {val2} são iguais')