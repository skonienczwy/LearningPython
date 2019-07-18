from UtilidadesCeV.moeda85 import metade,dobro,aumentar,diminuir,formata
print('##Exercicio 85##')

valor = float(input('Digite o preço R$ '))
print(f'A metade de R${formata(valor)} é R${metade(valor,False)}')
print(f'O dobro de R${formata(valor)} é R${dobro(valor,True)}')
print(f'Aumentando 10% de R${formata(valor)} é R${aumentar(valor,False)}')
print(f'Diminuindo 13% de R${formata(valor)} é R${diminuir(valor,True)}')