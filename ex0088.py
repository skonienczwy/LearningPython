from colorama import Fore, Back, Style

print('##Exercicio 88##')


def leiaInt(num):
    while True:
        try:
         t = int(input(num))
         return t


        except ValueError as erro:
                print(f'O Erro for causado por {erro.__class__}')

                print(Fore.RED + 'ERRO! Digite um número Inteiro válido:')
                print(Style.RESET_ALL)
        except EOFError as erro:

            print(Fore.RED + f'Não há dados inseridos pelo usuário, Erro foi identificado como: {erro.__class__}')
            exit()




def leiaFloat(num):
    while True:
        try:
            t = float(input(num))
            return t
        except ValueError as erro:
                print(f'O Erro for causado por {erro.__class__}')
                print(Fore.RED + 'ERRO! Digite um número Real válido:')
                print(Style.RESET_ALL)
        except EOFError as erro:
                print(Fore.RED + f'Não há dados inseridos pelo usuário, Erro foi identificado como: {erro.__class__}')
                print(Style.RESET_ALL)
                exit()




n = leiaInt('Digite Um numero Inteiro: ')
n2 = leiaFloat('Digite Um numero Real: ')
print(f'Você digitou o número inteiro {n} e o número real {n2} ')

