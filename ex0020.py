print('##Exercicio 20##')

valorProduto = float(input('Insira valor do produto: '))

opcao = int(input(f'Qual a forma de pagamento : ' '\n' 
                  '1 - Dinheiro ou Cheque' '\n'
                  '2 - A vista no cartão' '\n'
                  '3 - 2x no cartão' '\n'
                  '4 - 3x ou mais \n'))

if opcao == 1 :
    valorProduto2 = valorProduto - (valorProduto * (0.10))
    print(f'Você escolheu a opção Dinheiro ou Cheque e o valor original é de R${valorProduto:.2f}, '
          f'e você terá um de 10% : R${valorProduto2:.2f}')
elif opcao == 2:
    valorProduto2 = valorProduto - (valorProduto * (0.05))
    print(f'Você escolheu a vista no cartão e o valor original é de R${valorProduto:.2f},'
          f' e você terá um desconto 5% : R${valorProduto2:.2f}')
elif opcao == 3:
    print(f'Você escolheu a opção 2x o valor a pagar será de R${valorProduto:.2f}, '
          f'não há descontos para esta opção de pagamento ')
elif opcao == 4:
    valorProduto2 = valorProduto + (valorProduto * (0.30))
    print(f'Você escolheu a opção 3x ou mais e o valor original é de R${valorProduto:.2f},'
          f' e esta opção acrescenta 30% de juros ao valor: R${valorProduto2:.2f}')
else:
    print('Esta opção não existe')