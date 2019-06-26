from datetime import datetime
print('##Exercicio 68##')

cadastro = dict()

cadastro['Nome'] = str(input('Insira o nome : '))
nascimento = int(input('Insira o ano de nascimento : '))
cadastro['Idade'] = datetime.now().year - nascimento
cadastro['CTPS'] = int(input('Carteira de trabalho (0 se não tiver) : '))


if cadastro['CTPS'] == 0 :
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f'{k} tem o valor de {v}')
    
    print('-=' *30)
    exit()

cadastro['Contratação'] = int(input('Ano de contratação : '))
cadastro['Salário'] = float(input('Salário : '))
cadastro['Aposentadoria'] = (cadastro['Contratação'] - nascimento) + 35

print('-=' *30)
for k,v in cadastro.items():
    print(f'{k} tem o valor de {v}')

print('-=' *30)