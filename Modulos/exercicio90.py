from colorama import Fore,Style

def mostrarMenu():
        print('-'*30)
        print('MENU PRINCIPAL')
        print('-' * 30)
        print(Fore.LIGHTYELLOW_EX +'1 -'+ Style.RESET_ALL + Fore.LIGHTBLUE_EX +' Ver Pessoas Cadastradas' +  Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX +'2 -'+ Style.RESET_ALL + Fore.LIGHTBLUE_EX +' Cadastrar Pessoas' + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX +'3 -'+ Style.RESET_ALL + Fore.LIGHTBLUE_EX +' Sair do Sistemas' + Style.RESET_ALL)



def cadastrar(nome,idade):


        ##Com with o arquivo é fechado automaticamente sem necessidade do close
        with open('cadastro.txt', 'a') as f:

                f.write(nome+'\t' )
                idade2 =  str(idade)
                f.write(idade2 + ' anos\n')


        # ##Maneira tradicional de manusear arquivos
        # f = open('cadastro.txt','a')
        # f.write(nome + ',')
        # idade2 = str(idade)
        # f.write(idade2)
        # f.close()




def verCadastro():
        with open('cadastro.txt', 'r') as f:
                for i in f:
                        print(i)


