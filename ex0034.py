import random
import time
print('##Exercicio 34##')
print("Escolha um núumero de 0 á 10 \n")
advinha = -1
n = -2
palpites = 0


while n != advinha:
    n = random.randint(0, 10)
    advinha = int(input("Em que número Pensei?  "))
    print("Processando...")
    time.sleep(1)
    palpites +=1
    if n == advinha:
        break
    print(f"Ganhei, pensei em {n} e você digitou {advinha}")

print(f"Finalmente você acertou depois de {palpites} tentativas, sua escolha foi {advinha} X {n} Escolha do Computador ")

