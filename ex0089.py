import requests
from colorama import Fore, Back, Style
print('##Exercicio 89#')



try:
    response = requests.get('http://www.pudim.com.br')
    print(Fore.GREEN + 'URL Está acessível')
    print(Style.RESET_ALL)
except Exception as error:
    print(Fore.RED + 'ERRO! URL não está acessível')
    print(Style.RESET_ALL)




#Checa o código do request(200,404,etc)
# print(response)