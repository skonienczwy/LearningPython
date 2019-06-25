import random
from time import  sleep
print('##Exercicio 67##')

jogadores = dict()
print('VALORES SORTEADOS')
for i in range(1,5):
    jogadores[f'Jogador {i}'] = random.randint(1, 6)

for k,v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(1)

print('=-'*30)
print(f'Todas as jogadas {jogadores}')
print('=-'*30)
print('RANKING DOS JOGADORES')
##########SORT DICTIONARY##########
count = 1
for item in sorted(jogadores, key = jogadores.get, reverse=True):
    print (f'{count}º : {item} tirou {jogadores[item]}')
    count += 1
    sleep(1)

