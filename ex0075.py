import random
from time import sleep
print('##Exercicio 75##')

numeros = list()

def maior(randomico):
    print('=-' * 30)
    print('Analisando os valores passados')
    print(f'Foram informados {randomico} valores ao todo')
    if randomico == 0:
     print('Valor 0 ele é o maior número')
    else:

        for i in range(0,randomico):
            numeros.append(random.randint(0,10))
            maior = max(numeros)
            print(numeros[i],end=' ')
            sleep(1)
        print(f'Maior Numero foi : {maior}')
        print('=-' * 30)
        numeros.clear()




maior(6)
maior(3)
maior(2)
maior(1)



