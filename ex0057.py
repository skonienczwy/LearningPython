print('##Exercicio 57##')

lista = []
while True:

    val = int(input('Insira um valor: '))
    lista.append(val)
    while True:
        op = str(input('Deseja inserir mais valores? S/N'))
        if op in 'Ss':
            break
        else:
            print(f'Esta é a lista original {lista}')
            print(f'Foram digitados {len(lista)} elementos')
            print(sorted(lista,reverse=True))
            if 5 in lista:
             print(f'O número 5 foi digitado na lista')
            exit()
