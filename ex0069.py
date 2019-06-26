print('##Exercicio 69##')

jogador = dict()
gols = list()

jogador['Nome'] = str(input('Nome do Jogador: '))

partidas  = int(input(f'Quantas partidas {jogador["Nome"]} jogo?  '))


for i in range(0,partidas):
    gol = int(input(f'Quantos gols {jogador["Nome"]} marcou no jogo {i+1} : '))
    gols.append(gol)
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-=' * 30)

print(f'O Jogador {jogador["Nome"]} jogou {partidas} partidas.')


for i in range(0,len(jogador["Gols"])):
    print(f'Na partida {i+1} ele fez {jogador["Gols"][i]}')


print(f'Foi um total de {sum(jogador["Gols"])} gols.')
print('-=' * 30)