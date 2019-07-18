from UtilidadesCeV.moeda84 import metade,dobro,aumentar,diminuir,formata
print('##Exercicio 84##')

valor = float(input('Digite o preço R$ '))
print(f'A metade de R${formata(valor)} é R${metade(valor)}')
print(f'O dobro de R${formata(valor)} é R${dobro(valor)}')
print(f'Aumentando 10% de R${formata(valor)} é R${aumentar(valor)}')
print(f'Diminuindo 13% de R${formata(valor)} é R${diminuir(valor)}')