print('##Exercicio 49##')


colocacao = ('Palmeiras','Atlético-MG','Santos','Flamengo','Internacional','Bahia','Botafogo',
             'São Paulo','Corinthians','Athletico-PR','Ceará','Goiás','Chapecoense','Fortaleza',
             'Cruzeiro','Fluminense','CSA','Grêmio','Avaí','Vasco')


print('#'*20)
print('TABELA BRAZILEIRAO')
print('#'*20)
print(colocacao)
print(f'Os 5 primeiros são: {colocacao[:5]} ')
print(f'Os 4 últimos são: {colocacao[16:20]} ')
print(f'Times em ordem alfabética: {sorted(colocacao)} ')
index = colocacao.index('Chapecoense')
print(f'A Chapecoense esta na posição : {index +1} ')