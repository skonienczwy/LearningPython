print('##Exercicio 62##')

matriz = list()
linha0 = list()
linha1 = list()
linha2 = list()


for i in range(0,3):
    val = int(input(f'Insira valor em [0][{i}] : '))
    linha0.append(val)
matriz.append(linha0[:])
for i in range(0,3):
    val = int(input(f'Insira valor em [1][{i}]:'))
    linha1.append(val)
matriz.append(linha1[:])
for i in range(0,3):
    val = int(input(f'Insira valor em [2][{i}]:'))
    linha2.append(val)
matriz.append(linha2[:])





for i in range(0,3):
    print(matriz[i])
