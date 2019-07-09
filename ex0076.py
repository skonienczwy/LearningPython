import random
from time import sleep
print('##Exercicio 76##')

numeros = list()

def sorteia():
    print(f'Sorteando cinco valores da lista :')
    for i in range(0,5):
        numeros.append(random.randint(0,50))
        print(numeros[i], end=' ')
        sleep(1)

def somaPares():
    print()
    soma = 0
    for i in numeros:
        if i % 2 == 0 :
            soma += i


    print(f'A soma dos pares é {soma}')

sorteia()
somaPares()