import re

from UtilidadesCeV.Dado.leiadinheiro import leiaDinheiro
from UtilidadesCeV.Moeda.moeda86 import resumo

print('##Exercicio 87##')
p = leiaDinheiro('Digite o preço R$')

resumo(p,50,30)