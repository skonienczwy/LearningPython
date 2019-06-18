print('##Exercicio 28##')


n = int(input('Insira um Número: '))
primos = 0

for c in range(1,n+1):
        if n % c == 0:
         primos +=1

if primos > 2:
    print(f'Número {n} não é primo')
elif n ==1:
    print(f'Número {n} não é primo')
else:
    print(f'Número {n} é primo')
