print('##Exercicio 81##')

def notas(*num,sit=False):
    '''

    :param num: Notas de entrada, não há limites de notas cadastradas.
    :param sit: False não mostra situação True Mostra situação que pode ser BOA,RAZOÁVEL ou RUIM.
    :return: Retorna o dicionário com os dados inseridos na váriavel num.
    '''

    registro = dict()


    registro['Total'] = len(num)
    registro['Maior'] = max(num)
    registro['Menor'] = min(num)
    registro['Media'] = sum(num)/len(num)

    if sit == False:
        return registro
    else:

        if registro['Media'] < 50 :
            registro['Situação'] = 'RUIM'
        elif registro['Media'] > 50 and registro['Media'] < 70:
            registro['Situação'] = 'RAZOÁVEL'
        else:
            registro['Situação'] = 'BOA'
        return registro

    print(registro)


resp = notas(30,100,30,30,30,sit=True)
print(resp)
# help(notas)