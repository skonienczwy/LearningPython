print('##Exercicio 70##')


pessoas = dict()
listaPessoas = list()

while True:

    pessoas['Nome'] = str(input('Insira o nome: '))
    pessoas['Sexo'] = str(input(f'Insira o Sexo de {pessoas["Nome"]}: '))
    pessoas['Idade'] = int(input(f'Insira a idade de {pessoas["Nome"]}: '))
    listaPessoas.append(pessoas.copy())


    while True:
        op = str(input('Deseja cadastrar outra pessoa [S/N] ?'))
        if op in 'Ss':

            break
        else:

            print('Fim Programa:')
            print(f'Foram cadastradas um total de {len(listaPessoas)} pessoas.')
            media = aux = count = 0

            # print(listaPessoas)

            for i in range(0,len(listaPessoas)):
                aux = listaPessoas[i]["Idade"]

                media += aux

                count +=1
            media = media / count
            # print(listaPessoas[0]["Idade"])
            print(f'A média de idade é de {media} anos')
            print('As mulheres cadastradas foram :',end=' ')
            for i in range(0,len(listaPessoas)):
                if listaPessoas[i]["Sexo"] in 'Ff':
                    print(f'{listaPessoas[i]["Nome"]}',end=' ')
            print()
            print('As Pessoas acima da média são: ',end=' ')
            for i in range(0,len(listaPessoas)):

                if listaPessoas[i]["Idade"] > media:
                    print(f'{listaPessoas[i]["Nome"]}', end=' ')
            print()
            print('FIM DO PROGRAMA')
            exit()





