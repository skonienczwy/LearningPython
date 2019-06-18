print('##Exercicio 41##')

num = []
n = int(input('Insira um valor: '))
num.append(n)

while True:

    x = str(input('Deseja continuar inserindo valores? '))
    if x in 'Ss':
        n = int(input('Insira um valor: '))
        num.append(n)
        print(num)
    else:
        break

media = sum(num)/len(num)
minimo = min(num)
maximo = max(num)

print(f'Estes são todos os valores digitados: {num}')
print(f'A media dos valores digitados é de: {media}')
print(f'O menor valor digitado é: {minimo}')
print(f'O Maior valor digitado é: {maximo}')