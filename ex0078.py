print('##Exercicio 78##')



def fatorial(fatorial, show=False):
    '''

    :param fatorial: Numero que deseja ver o fatorial
    :param show: Parametro Opcional para ver o calculo
    :return: Resultado ou calculo inteiro com resultado
    '''
    n =fatorial
    for i in range(1, fatorial):
        fatorial *= i


    if show == False :

        return fatorial
    else:
        print(f'!{n} =',end=' ')
        for i in range(n,0,-1):
            print(f'{i} x',end=' ' )
        print('=', end=' ')
        return fatorial

print(fatorial(5,True))
help(fatorial)



