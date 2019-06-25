print('##Exercicio 66##')

aluno = dict()


nome = str(input('Nome: '))
media = float(input(f'Media de {nome}: '))
print('=-'*15)

if media >= 70:
    situacao = 'Aprovado'

elif media >= 50 and media < 70:
    situacao = 'Recuperação'

else:
    situacao = 'Reprovado'


aluno = {'Nome': nome, 'Media': media,'Situação': situacao}



for k,v in aluno.items():
    print(f'{k} é igual á {v}')





