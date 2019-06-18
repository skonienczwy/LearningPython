import random
print('##Exercicio 21##')

opcao = int(input('Escolha : \n'
                    '1 - Pedra\n'
                    '2 - Papel\n'
                    '3 - Tesoura\n'))

opcoes = ['Pedra', 'Papel', 'Tesoura']
opcao2 = random.choice(opcoes)


if opcao==1 and opcao2=='Pedra':
    print(f'Pedra contra {opcao2} = Empate')
elif opcao==1 and opcao2=='Papel':
    print(f'Pedra contra {opcao2} = Você perdeu, Papel cobre Pedra')
elif opcao == 1 and opcao2 == 'Tesoura':
    print(f'Pedra contra {opcao2} = Você Ganhou, Pedra Quebra Tesoura')

elif opcao == 2 and opcao2=='Pedra':
    print(f'Papel contra {opcao2} = Você ganhou, Papel cobre Pedra')
elif opcao == 2 and opcao2=='Papel':
    print(f'Papel contra {opcao2} = Empate')
elif opcao == 2 and opcao2 == 'Tesoura':
    print(f'Papel contra {opcao2} = Você Perdeu, Tesoura corta Papel')

elif opcao == 3 and opcao2=='Pedra':
    print(f'Tesoura contra {opcao2} = Você Perdeu, Pedra quebra Tesoura')
elif opcao == 3 and opcao2=='Papel':
    print(f'Tesoura contra {opcao2} = Você Ganhou, Tesoura corta Papel')
elif opcao == 3 and opcao2 == 'Tesoura':
    print(f'Tesoura contra {opcao2} = Empate')

else:
    print('Esta opção não existe')

##print(random.choice(opcao2))
