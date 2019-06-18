print('##Exercicio 32##')
soma=0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
mulheres = 0

for c in range(1,5):
    pessoa = str(input(f'Insira o Nome da pessoa número {c} : '))
    idade = int(input(f'Insira a  idade de  {pessoa} : '))
    sexo = str(input(f'Qual o sexo de {pessoa} ? M/F : '))
    soma+=idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem=idade
        nomeHomemMaisVelho=pessoa
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = pessoa
    if sexo in 'Ff' and idade < 20:
         mulheres += 1
media =soma/4

print(f'A media de idade das pessoas é de {media}')
print(f'O nome do homem mais velho é  {nomeHomemMaisVelho} e sua idade é de {maiorIdadeHomem}')
print(f'O total de mulheres com menos de 20 anos é de {mulheres}')

