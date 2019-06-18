print('##Exercicio 38##')

pa = []

class Progressao:

    def __init__(self, p1, razao):
        self.p1 = p1
        self.razao = razao



    def calculo(self):
        count = 0
        while count != 10:
            pa.append(self.p1)
            #print(f'{self.p1}', end=' ')
            self.p1 += self.razao

            count += 1


primeiro_termo = int(input("Insira o primeiro termo da PA: "))
razaoPA = int(input("Insira a razão da PA: "))

resultado = Progressao(primeiro_termo,razaoPA,)
resultado.calculo()

print(f" Os 10 Primeiros termos da PA são : {pa}")


while True:

    n2 = int(input("Quantos termos adicionais gostaria de visualizar? "))
    if n2 == 0:
        print("Fim do Programa!")
        exit()

    else:

        n = pa[-1]
        r = pa[-1] - pa[-2]

        t = len(pa)
        for c in range(t, len(pa)+n2):
         n += r
         pa.append(n)

    print(pa)