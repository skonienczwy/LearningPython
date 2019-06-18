print('##Exercicio 27##')


n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))

decimo = n +(10-1) *r

print('Os 10 Primeiros termos da Progressão Aritmética são: {',end="")

for c  in range(n,decimo+r,r):

     print(f'{c}', end="," )

print('}')
