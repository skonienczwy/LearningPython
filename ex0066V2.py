print('##Exercicio 66##')

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
print('=-'*15)
print('=-'*15)
if aluno['Media'] >= 70:
    situacao = 'Aprovado'
elif aluno['Media'] >= 50 and aluno['Media'] < 70 :
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

aluno['Situação'] = situacao

for k,v in aluno.items():
    print(f'{k} é igual á {v}')