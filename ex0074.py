from time import sleep
print('##Exercicio 74##')


def contagem(ini, fim, passo):
    print(f'CONTAGEM DE {ini} ATÉ {fim} DE {passo} em {passo}')
    for i in range(ini,fim,passo):
        print(i, end=' ')
        sleep(1)
    print(fim)
    print('FIM!')
    print('=-' * 30)


contagem(1, 10, 1)
contagem(10, 1, -1)
# contagemAuto()
print('Agora é sua vez de personalizar a Contagem')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

if i < f and p ==0 :
    p = 1
if i > f and p == 0 :
    p = -1
contagem(i, f, p)