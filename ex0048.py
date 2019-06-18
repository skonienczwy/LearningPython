print('##Exercicio 48##')

numeros = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE',
           'TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZOITO','DEZENOVE','VINTE')

while True:
    escolha = int(input('Insira um Numero: '))

    if escolha < 0 or escolha > 20:
        print('Escolha um Número entre 0 e 20')
    else:
        print(numeros[escolha])
        exit()


