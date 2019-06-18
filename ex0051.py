print('##Exercicio 51##')

lista = []
count = 0
pares = []
for c in range(0,4):
 val = int(input('Insira um Valor: '))
 lista.append(val)

t = tuple(lista)


print(f'O número 9 Apareceu : {t.count(9)} vezes.')

if 3 in t:
 print(f'O número 3  Apareceu na posicao: {t.index(3)+1}')

else:
 print('Não há o número 3')

for i in range(0,4) :
 if t[i] % 2 == 0:
   pares.append(t[i])

# print(lista)
# print(t)


print(f'Números pares: {pares}')