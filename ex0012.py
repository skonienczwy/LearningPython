print('##Exercicio 12##')

casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o valor do seu salario: '))
tempo = (int(input('Em quantos anos gostaria de pagar a casa : '))*12)



casaValMensal = casa/tempo

if casaValMensal/salario <= 0.30:
    print(f'Credito Aprovado : O Valor total da casa é de R$ {casa:.2 f} com mensalidades de R${casaValMensal:.2f}')
else:
    print(f'Credito Negado : O Valor total da casa é de R$ {casa:.2f} e as mensalidades excedem 30% do seu rendimento')

