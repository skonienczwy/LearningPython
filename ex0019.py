print('##Exercicio 19##')

altura = float(input('Insira sua Altura: '))
peso = float(input('Insira seu Peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e significa que você está abaixo do peso')
elif imc >= 18.5  and imc < 25:
    print(f'Seu IMC é de {imc:.2f} e significa que você está no peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f} e significa que você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é de {imc:.2f} e significa que você está obeso')
else:
    print(f'Seu IMC é de {imc:.2f} e significa que você está com obesidade mórbida')

