print('##Exercicio 39##')

fibo = [0,1,1]

class Fibo():

    def __init__(self, n):
        self.n = n

    def calc(self):
        count = 0

        while count != self.n:
            r = fibo[-1] + fibo[-2]
            fibo.append(r)



            count += 1

n = int(input(" Quantos números de Fibonacci gostaria de visualizar? "))

if n == 1:
    print(f'[{fibo[0]}]')
elif n == 2:
    print(f'{fibo[0:2]}')
elif n == 3:
    print(f'{fibo}')
elif n == 0:
    print('Fim do Programa')
else:
    sequence = Fibo(n)
    sequence.calc()

n5 = len(fibo)
n5 = n5 -3
print(fibo[0:n5])
