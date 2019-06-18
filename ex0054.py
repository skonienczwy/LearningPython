print('##Exercicio 54##')

lista = []
menor=maior=0
for c in range(0,5):
    lista.append(int(input(f'Insira um valor na posição {c} :  ')))


maior = max(lista)
menor = min(lista)

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} e ele está na posições : ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} e ele está na posições : ',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()

print('Fim do Programa')


