print('##Exercicio 80##')

def leiaInt(num):

           while num is not int:
               t = input(num)
               if t.isnumeric():
                   t = int(t)
                   n = t

                   return n


               else:
                   from colorama import Fore, Back, Style
                   print(Fore.RED + 'ERRO! Digite um número inteiro válido:')
                   print(Style.RESET_ALL)



n = leiaInt('Digite Um numero: ')
print(f'Você digitou o número {n}')

