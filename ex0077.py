print('##Exercicio 77##')

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano

    if idade < 16:
        return f' Com {idade} anos : NÃO VOTA'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f' Com {idade} anos : VOTO OPCIONAL'
    else:
        return f' Com {idade} anos : VOTO OBRIGATÓRIO'

ano = int(input('Insira o no de nascimento: '))

print(voto(ano))