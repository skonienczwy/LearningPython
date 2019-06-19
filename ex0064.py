import  random
from time import sleep
print('##Exercicio 64##')

jogo = list()
palpites = list()

n = int(input('Quantos jogos gostaria de fazer? '))

for c in range(n):

 r = random.sample(range(1,60),6)
 jogo.append(sorted(r))
 palpites.append(jogo[:])

 jogo.clear()
 print(f'Jogo {c+1} : {palpites[c]}')
 sleep(1)
