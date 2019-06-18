print('##Exercicio 29##')

palavra = str(input('Insira uma palavra: '))
palavraSemEspaco = palavra.upper().replace(" ","")


if palavraSemEspaco == palavraSemEspaco[::-1]:
    print('A Palavra é um Palindromo')
else:
    print('A Palavra não é um Palindromo')


