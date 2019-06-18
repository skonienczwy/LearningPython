print('##Exercicio 43##')

while True:
    n = int(input('Digite o número que deseja ver a tabuada: '))
    if n < 0:
        break
        
    else:
        for i in range(0,11):
            result = n * i
            print(f'{i} x {n} = {result}')

print('Fim do Programa!!!')
