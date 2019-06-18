print('##Exercicio 42##')

num = []
count = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:

        break
    else:
        num.append(n)

    print(f'Os seguinte valores já foram digitados: {num} ')

result = sum(num)
count = len(num)-1

print(f'A soma dos valores digitados foi: {result} excluindo o valor 999, você digitou {count} números.')
print('Fim Do Programa')