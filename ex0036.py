from  math import factorial
print('##Exercicio 36##')



n = int(input('Insert a number: '))
f = 1
c = n

print(f'{n}! = ',end="")
while c > 0:
    print(f'{c}',end="")
    print(f' x ' if c > 1 else ' = ' ,end="")
    f = f * c
    c -= 1

print(f'{f}')