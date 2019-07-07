print('##Exercicio 72##')

def area(l, c):
    s = l * c
    print(f'A área de um terreno de {l}m² x {c}m² é de {s}m²')

l = float(input('LARGURA m²: '))
c = float(input('COMPRIMENTO m²: '))

area(l, c)