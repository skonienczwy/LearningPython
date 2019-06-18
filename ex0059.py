print('##Exercicio 59##')

expressao = ''



val = str(input('Insira a expressão: '))

esquerda = val.count('(')
direita =  val.count(')')


if esquerda == direita:
    print('Expressão Válida')
else:
    print('Expressão Inválida')

