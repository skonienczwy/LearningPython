from time import sleep
print('##Exercicio 74##')

def contagemAuto():
    print('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1')
    print('=-'*30)
    for i in range(0,11):
        print(i,end=' ')
        # sleep(1)
    print('FIM!')
    print('=-' * 30)
    print('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2')
    for i in range(10,-2,-2):
        print(i, end=' ')
        # sleep(1)
    print('FIM!')
    print('=-' * 30)

def contagem(ini, fim, passo):
    print(f'CONTAGEM DE {ini} ATÉ {fim} DE {p} em {passo}')
    for i in range(ini,fim,passo):
        print(i, end=' ')
        # sleep(1)
    print(fim)
    print('FIM!')
    print('=-' * 30)



contagemAuto()
print('Agora é sua vez de personalizar a Contagem')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

if i < f and p ==0 :
    p = 1
if i > f and p == 0 :
    p = -1
contagem(i, f, p)