print('##Exercicio 47##')

valor = int(input('Quanto Deseja Sacar? '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de Cedulas de {totCed} de R${ced}')
        if ced == 50:
             ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('Fim do Programa')

