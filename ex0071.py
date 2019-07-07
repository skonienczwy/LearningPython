print('##Exercicio 71##')

jogadores = list()
jogador = dict()
gols = list()


while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas  = int(input(f'Quantas partidas {jogador["Nome"]} jogo?  '))

    for i in range(0,partidas):
        gol = int(input(f'Quantos gols {jogador["Nome"]} marcou no jogo {i+1} : '))
        # jogador['Total'] = sum(jogador[i]["Gol"])
        gols.append(gol)
        jogador['Gols'] = gols.copy()
        jogador['Total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    print('-=' * 30)

    while True:
        op = str(input('Deseja Continuar? [S/N')).upper()[0]
        if op in 'Ss':
            break
        else:

            print(f'{"Nº":<4}{"NOME":<10}{"GOLS":>8}{"TOTAL":>8}')
            for c,i in enumerate(range(len(jogadores))):
                print(f'{c}  {jogadores[i]["Nome"]:<10} {str(jogadores[i]["Gols"]):>10} {jogadores[i]["Total"]}')
            while True:
                print('-' * 35)
                opc = int(input('Mostrar Detalhes de qual Jogador? '))
                if opc == 999:
                    print('Finalizando...')
                    break
                if opc <= len(jogadores) - 1:
                 gols = jogadores[opc]["Gols"]
                 print(f'O Jogador {jogadores[opc]["Nome"]} ')
                 for i in range(0,len(gols)):
                    print(f'No Jogo {i+1} fez {gols[i]} ')
            exit()

