print('##Exercicio 65##')


aluno = list()
auxiliar = list()
opcao = 0
while True:
    nome = str(input('Insira o nome do Aluno: '))
    auxiliar.append(nome)

    nota1 = int(input('Insira a primeira nota: '))
    auxiliar.append(nota1)
    nota2 = int(input('Insira a segunda nota: '))
    auxiliar.append(nota2)
    media = float((nota1 + nota2)/2)
    auxiliar.append(media)
    aluno.append(auxiliar[:])
    auxiliar.clear()

    while True:
        op = str(input('Deseja inserir mais valores? S/N'))
        if op in 'Ss':
            break
        else:
            print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')


            print('=-' * 15)
            for i,v in enumerate(aluno):

                print(f'{i:<4}  {v[0]:<10} {v[3]:>8.1f}')



            while opcao != 999:
                opcao = int(input('Mostar as notas de qual aluno?(999 Interrompe) '))
                if opcao == 999:

                        print('Fim do Programa')
                        exit()
                elif opcao > len(aluno)  and opcao != 999:
                        print('Opção errada')
                else:

                    print(f'Notas de {aluno[opcao][0]} são : {aluno[opcao][1:3]} ')




