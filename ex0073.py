print('##Exercicio 73##')

def escreva(texto):
    tam = len(texto)
    print('~'*tam)
    print(f'{texto}')
    print('~' * tam)

texto = str(input('Insira uma mensagem: '))

escreva(texto)
