import random
print('##Exercicio 50##')

num = ()
lista = []

for c in range(0,5):
    numero = random.randint(0, 10)
    lista.append(numero)

num = tuple(lista)
print(lista)
sort = sorted(num)
print(f'Menor valor é: {sort[0]}')
print(f'Maior valor é: {sort[-1]}')