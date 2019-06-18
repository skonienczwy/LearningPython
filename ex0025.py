print('##Exercicio 25##')

num = int(input('Insira o Número que deseja ver a tabuada: '))

for c in range(0,11):
    result = c * num
    print(f'{num} x {c} = {result}')