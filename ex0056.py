print('##Exercicio 56##')

lista = []

for c in range(0,5):

    n = int(input('Insira um Valor: '))
    if c == 0 or n > lista[-1]:
            lista.append(n)
            print('Adicionado ao Final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos}')
                break
            pos+=1

print(lista)