print('##Exercicio 53##')

palavras = ('JOAO', 'VITOR','SKONIENCZWY','BRASILEIRO','HOLANDA','ENGINEER')

for c in range(0,len(palavras)):
    palavra = palavras[c]
    vogais = []
    for i in range(0,len(palavra)):
        if palavra[i] in 'AaEeIiOoUu':
            vogais.append(palavra[i])
    print(f'A palavra {palavras[c]} tem as seguintes vogais: {vogais} ')
