print('##Exercicio 60##')
##Joao Solution

pessoas = list()
listaAux = list()
pesadas = list()
leves = list()
count = 0
minimo = list()
maximo = list()
name = list()

while True:
    val = str(input('Insira o Nome: '))
    listaAux.append(val)
    val = float(input('Insira o Peso: '))
    listaAux.append(val)
    op = str(input('Deseja Inserir mais pessoas ?  S/N')).upper()
    pessoas.append(listaAux[:])

    if listaAux[1] >= 50:
        pesadas.append(listaAux[:])
    else:
        leves.append(listaAux[:])
    listaAux.clear()

    while True:

        if op == 'S':
            break
        elif op == 'N':
            print()
            print(f'Foram Cadastradas {len(pessoas)} pessoas.')
            for i in leves:
                minimo.append(leves[count][1])
                count += 1
            count = 0
            for c in leves:
                if min(minimo) == leves[count][1]:
                    name.append(leves[count][0])
                count += 1
            print(f'O menor peso foi de {min(minimo)}kg. Peso de {name}', end='' '\n')


            name.clear()
            count = 0
            for i in pesadas:
                maximo.append(pesadas[count][1])
                count += 1
            count = 0
            for c in pesadas:
                if max(maximo) == pesadas[count][1]:
                    name.append(pesadas[count][0])
                count += 1
            print(f'O maior peso foi de {max(maximo)}kg. Peso de {name}', end='' '\n')

            print()

            exit()
        else:
            op = str(input('Deseja Inserir mais pessoas ?  S/N')).upper()



