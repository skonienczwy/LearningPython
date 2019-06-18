import operator
print('##Exercicio 46##')

vendas = {}

class Produtos():
    def __init__(self,produto,preco):
        self.produto = produto
        self.preco = preco

    def adiciona(self):
        vendas.update({prd: prc})



while True:
    prd = str(input('Insira o Produto: ').upper())
    prc = float(input(f'Qual é o preço do produto {prd} ? R$'))

    produtos = Produtos(prd,prc)
    produtos.adiciona()

    while True:
        op = str(input('Deseja Continuar? S/N \n' ).upper())
        if op == 'S':
            break
        else:
            print('###Resumo da compra### ')

            soma = sum(vendas.values())
            maisMil = list(filter(lambda x: x > 1000, vendas.values()))
            vendas = sorted(vendas.items(), key=operator.itemgetter(1))
            produtoBarato = str(vendas[0])
            virgula = produtoBarato.find(',')
            produto = produtoBarato[2:virgula-1]
            custo = produtoBarato[virgula+1:-1]




            print(f'Estas são suas compras: {vendas}')
            print(20*'-')
            print(f'O valor total das compras foi de R${soma:.2f}')
            print(20 * '-')
            print(f'Temos {len(maisMil)} custando mais de RS1000.00')
            print(20 * '-')
            print(f'O produto mais barato foi {produto} que custa R${custo}')

            exit()


