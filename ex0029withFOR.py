print('##Exercicio 29##')

frase = str(input('Insira uma palavra: '))
palavras = frase.upper().split()
junto = ''.join(palavras)
inverso =''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]


if junto == inverso:
        print(junto, inverso)
        print('A Palavra é um Palindromo')
else:
        print(junto, inverso)
        print('A Palavra não é um Palindromo')