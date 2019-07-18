from UtilidadesCeV.moeda83 import metade,dobro,aumentar,diminuir

print('##Exercicio 83##')

valor = float(input('Digite o preço R$ '))
print(f'A metade de R${valor} é R${metade(valor)}')
print(f'O dobro de R${valor} é R${dobro(valor)}')
print(f'Aumentando 10% de R${valor} é R${aumentar(valor)}')
print(f'Diminuindo 13% de R${valor} é R${diminuir(valor)}')