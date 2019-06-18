print('##Exercicio 55##')

lista= []
val = int(input('Insira um valor: '))
lista.append(val)
while True:

    x = str(input('Deseja continuar inserindo valores? S/N '))
    if x in 'Ss':
        val = int(input('Insira um valor: '))
        if val in lista:
            print('Este valor já Existe e não será Adicionado.')
        else:
            lista.append(val)
            print('Valor adicionado com sucesso')
    else:
        
        print(f'Valores digitados foram {lista.sort()} ')
        exit()

