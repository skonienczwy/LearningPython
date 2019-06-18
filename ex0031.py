print('##Exercicio 31##')

pesos = []
for c in range(1,6):
    peso = float(input(f'Insira o peso da pessoa número {c} : '))
    pesos.append(peso)
    pesos.sort()

print(pesos)
print(f'O Menor peso é de {pesos[0]} e o maior peso é de {pesos[4]}')
