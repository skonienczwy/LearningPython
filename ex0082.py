from time import sleep
print('##Exercicio 82##')

colors = (  '\033[m',
            '\033[7;30;41m',
            '\033[0:30;42m',
            '\033[0:30;43m',
            '\033[0:30;44m',
            '\033[0:30;45m',
            '\033[7:30m;'
          )

def ajuda(f):

    carac = len(f)
    carac+=35
    print('~' * carac)
    print(f'{colors[5]}ACESSANDO O MANUAL DO COMMANDO "{f}"')
    print(f'{colors[0]}~' * carac)
    sleep(1)
    help(f)

while True:


    print(f'{colors[1]}~' * 27)
    print('SISTEMA DE AJUDA PYHELP ')
    print(f'{colors[0]}~' * 27)


    f = str(input('Função ou Biblioteca: '))
    if f.upper() == 'FIM':
        print('Fim do Programa')
        exit()
    else:
        ajuda(f)

