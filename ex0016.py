print('##Exercicio 16##')

nota1 = float(input('Informe a nota do primeiro semestre: '))
nota2 = float(input('Informe a nota do segundo semestre: '))

media = float((nota1 + nota2)/2)

if media < 50:
    print(f' Sua média foi {media} -  Aluno Reprovado')
elif media >= 50 and media <=69:
    print(f'Sua média foi {media} - Aluno em Recuperação')
else:
    print(f'Sua média foi {media} - Aluno Aprovado')