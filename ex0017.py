from datetime import datetime
print('##Exercicio 17##')

nascimento = int(input('Informe a data do nascimento: '))
anoAtual = datetime.now()

idade = anoAtual.year - nascimento

if idade <= 9:
    print(f'A idade do aluno é de {idade} anos. Categoria: MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'A idade do aluno é de {idade} anos. Categoria: INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'A idade do aluno é de {idade} anos. Categoria: JUNIOR')
elif idade == 20:
    print(f'A idade do aluno é de {idade} anos. Categoria: SÊNIOR')
else:
    print(f'A idade do aluno é de {idade} anos. Categoria: MASTER')
