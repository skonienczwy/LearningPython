print('##Exercicio 79##')

def jogador(nome ='<desconhecido>' ,gols = 0):

    print( f'O Jogador {nome} fez {gols} gol(s) no campeonato.')

n = input('Nome do Jogador: ')
g = input('Quantidade de gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0
'Strip remove all spaces'
if n.strip() == '':
    jogador(gols = g)
else:
    jogador(n,g)