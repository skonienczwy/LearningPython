print('##Exercicio 81##')

def notas(*num,sit=False):
    dados = list()
    registro = dict()
    for i in (0,*num):
        dados.append(i)
    dados.remove(0)
    count = len(dados)
    som   = sum(dados)
    avg   = som/count

    registro['Total'] = len(dados)
    registro['Maior'] = max(dados)
    registro['Menor'] = min(dados)
    registro['Media'] = avg

    if sit == False:
        return f'{registro}'
    else:

        if avg < 50 :
            registro['Situação'] = 'RUIM'
        elif avg > 50 and avg < 70:
            registro['Situação'] = 'RAZOÁVEL'
        else:
            registro['Situação'] = 'BOA'
        return f'{registro}'

    print(registro)


resp = notas(100,72,80,80,80,100,70,30,100,30,30,30,sit=True)
print(resp)