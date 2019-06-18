from datetime import datetime
print('##Exercicio 15##')

nascimento = int(input('Informe a data do seu nascimento: '))
anoAtual = datetime.now()

alistamento = anoAtual.year - nascimento

if alistamento <=17:
    print(f'Sua idade é de {alistamento} anos, você ainda não precisa se alistar ')
elif alistamento == 18:
    print(f'Sua idade é de {alistamento} anos, você deve se alistar ')
else:
    print(f'Sua idade é de {alistamento} anos, passou da hora de você se alistar amigão.')
