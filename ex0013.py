print('##Exercicio 13##')
inteiro = int(input('Digite um número inteiro: '))

opcao = int(input(f'Deseja conver ter o numero {inteiro} em:' '\n' 
                  '1 - Binario' '\n'
                  '2 - Octal' '\n'
                  '3 - Hexadecimal' '\n'))

if opcao == 1:
    print(f' O numero {inteiro} convertido em binario é: {bin(inteiro)[2:]}')
elif opcao == 2:
    print(f' O numero {inteiro} convertido em octal é: {oct(inteiro)[2:]}')
elif opcao ==3:
    print(f' O numero {inteiro} convertido em Hexadecimal é: {hex(inteiro)[2:]}')
else:
    print('MULA!!! So tem 3 opçoes e vc ainda digita errado')