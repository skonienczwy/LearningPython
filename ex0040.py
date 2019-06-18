print('##Exercicio 40##')

num = []
count = 0
while True:
    n = int(input('Digite um Número: '))
    if n == 999:
        num.append(n)
        break
    else:
        num.append(n)

    print(f'Os seguinte valores já foram digitados: {num} ')

result = sum(num)-999
print(f'A soma dos valores digitados foi: {result} excluindo o valor 999')
print('Fim Do Programa')