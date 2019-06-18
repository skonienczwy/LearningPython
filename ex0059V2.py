print('##Exercicio 59##')
pilha = []

expr = str(input('Insira a expressão: '))

for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressão é válida!')
else:
    print('Sua expressão é inválida')

