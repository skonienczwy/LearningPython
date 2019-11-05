from Modulos.exercicio90 import mostrarMenu,cadastrar,verCadastro
from colorama import Fore,Style

print('##Exercicio 90#')


op = 0
while True:
    mostrarMenu()
    try:
        print('-' * 30)
        op = int(input(Fore.LIGHTYELLOW_EX + 'Sua opção: '+ Style.RESET_ALL))
        print('-' * 30)

        if op == 1:

            verCadastro()
        elif op == 2:
            print('###NOVO CADASTRO###')
            nome = str(input('Insira o nome: '))
            idade = int(input(f'Insira a idade de {nome}: '))
            cadastrar(nome,idade)

        elif op ==3:
            print('Fim do programa')

            exit()
        else:
            print('Insira uma opção válida')
            print()



    except ValueError as error:
        print(Fore.RED + 'Você inseriu um tipo/caracter diferente do permitido')
        print(Fore.RED + f'Este foi o erro: {error}')
        print(Style.RESET_ALL)
