print('##Exercicio 45##')

mulheres = []
homens = []

while True:

    idade = int(input('Insira a idade: '))
    while True:
        sexo = str(input('Insira o sexo da pessoa: ').upper())
        if sexo in 'MF':
            break
    if sexo =='F':
        mulheres.append(idade)
    if sexo == 'M':
        homens.append(idade)
    while True:
        op = str(input('Deseja Continuar? S/N').upper())
        if op == 'S':
            break
        else:

            homens18 = list(filter(lambda x: x > 18, homens))
            mulheres18 = list(filter(lambda x: x > 18, mulheres))
            mulheres20 = list(filter(lambda x: x < 20, mulheres))

            maiores = len(homens18) + len(mulheres18)


            print(f'Existem {maiores} pessoas maiores de 18 anos.')
            print(f'Foram cadastrados {len(homens)} homens.')
            print(f'Existem {len(mulheres20)} mulheres cadastradas com menos de 20 anos.')

            print('Fim do Programa!!')
            exit()



