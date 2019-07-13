print('##Exercicio 79##')

def jogador(nome,gols):

    if  not nome:
     nome = '<desconhecido>'

    return f'O Jogador {nome} fez {gols} gol(s) no campeonato.'

n = input('Nome do Jogador: ')
g = input('Quantidade de gols: ')

if g == '' or isinstance(g,str):

    g = 0
    int(g)

print(jogador(n,g))