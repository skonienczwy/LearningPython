print('##Exercicio 47##')

count1 = count10 = count20 = count50 = tot = 0

val = int(input('Quanto Deseja Sacar? '))


if val > 50:
    count50 = val // 50
    val = val - (count50 * 50)
    #print(val)

if val > 20:
    count20 = val // 20
    val = val - (count20 * 20)

if val > 10:
    count10 = val // 10
    val = val - (count10 * 10)

count = str(val)
count1 = int(count[-1])
tot = (count50*50) + (count20*20) + (count10*10) + count1
print(20*'#')
print(f'Total de {count50} cédulas de R$50,00')
print(f'Total de {count20} cédulas de R$20,00')
print(f'Total de {count10} cédulas de R$10,00')
print(f'Total de {count1} cédulas de R$1,00')
print(f'Valor total sacado R${tot} ')