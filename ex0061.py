print('##Exercicio 61##')

numeros = list()
pares = list()
impares = list()

for i in range(0,7):
    val = int(input(f'Insira o {i+1}º valor da lista:  '))
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)

print(pares)
print(impares)

numeros.append(pares[:])
numeros.append(impares[:])

print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
