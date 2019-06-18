print('##Exercicio 58##')

lista = []
pares = []
impares = []

while True:

    val = int(input('Insira um valor: '))
    lista.append(val)
    while True:
        op = str(input('Deseja inserir mais valores? S/N'))
        if op in 'Ss':
            break
        else:
            for c in range(len(lista)):
                if lista[c] % 2 == 0:
                    pares.append(lista[c])
                else:
                    impares.append(lista[c])

        print(f'Lista Original {lista}')
        print(f'Lista de Pares {pares}')
        print(f'Lista de Impares  {impares}')
        print('#'*30+ 'Fim do programa' + '#'*30)
        exit()