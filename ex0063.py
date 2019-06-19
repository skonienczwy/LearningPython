print('##Exercicio 63##')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColumn = maximo = 0

for l in range(0, 3):

    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}] : '))

print('-=' * 30)


maximo = matriz[1][0]
for l in range(0, 3):

    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        if  matriz[1][c] > maximo:
            maximo = matriz[1][c]
        print(f'[{matriz[l][c]:^5}]', end='')


    somaColumn += matriz[l][2]

    print()

print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna  é {somaColumn}')
print(f'O maior valor da segunda linha é  {maximo}')