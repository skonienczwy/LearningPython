import random
print('##Exercicio 44##')

vitorias = 0
while True:

    escolha = str(input('Par ou Ímpar?').upper())

    seuNumero = int(input('Escolha um número entre 0 á 10: '))
    pcNumero = random.randint(0, 10)
    total = seuNumero + pcNumero


    if total == 0 :
        print(f'Nínguem Ganha!')
    elif total % 2 == 0 and escolha == 'P':
        print(f'VocÊ ganhou porque {total} é PAR. ')

    elif total % 2 != 0 and escolha == 'I':
        print(f'VocÊ ganhou porque {total} é ÍMPAR. ')

    else:
        print(f'Você perdeu {total}')
        break

    vitorias += 1
print(f'Você venceu {vitorias} consecutivas')