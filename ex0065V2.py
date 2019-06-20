print('##Exercicio 65##')

aluno = list()


while True:
    nome = str(input('Insira o nome do Aluno: '))
    nota1 = int(input('Insira a primeira nota: '))
    nota2 = int(input('Insira a segunda nota: '))
    media = float((nota1 + nota2)/2)
    aluno.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' *26)

for i,a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *35)
    opc = int(input('Mostrar notas de qual aluno? '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc<= len(aluno) -1 :
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')

print('FIM DO PROGRAMA')
