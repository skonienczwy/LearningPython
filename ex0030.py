from datetime import datetime
print('##Exercicio 30##')

anoAtual = datetime.now()
cont = 0
cont2 = 0

for c in range(1,8):
    ano = int(input(f'Insira o ano do  nascimento da pessoa número {c} : '))
    maioridade = anoAtual.year - ano
    if maioridade >=18:
        cont +=1
    else:
        cont2 +=1

print(f'{cont} Atingiram a maioridade')
print(f'{cont2} Não atingiram a maioridade')