print('##Exercicio 37##')


n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))

count = 0

print('Os 10 Primeiros termos da Progressão Aritmética são: {', end="")
while count != 10:
        print(f'{n}', end=' ')
        n += r
        count += 1


print('}')

