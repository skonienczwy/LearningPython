from Modulos import moeda

print('##Exercicio 83##')

valor = float(input('Digite o preço R$ '))
print(f'A metade de R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}')
print(f'Aumentando 10% de R${valor:.2f} é R${moeda.aumentar(valor):.2f}')
print(f'Diminuindo 13% de R${valor:.2f} é R${moeda.diminuir(valor):.2f}')