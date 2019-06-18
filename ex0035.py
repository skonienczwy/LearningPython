print('##Exercicio 35##')

n1 = int(input('Insert the first number: '))
n2 = int(input('Insert the second number: '))
result = 0
count = 0

while count != 5:
    count = int(input('1 - Sum \n'
                      '2 - Multiple \n'
                      '3 - Biggest Number \n'
                      '4 - New Numbers \n'
                      '5 - Exit the Software \n'))
    if count == 1:
        result = n1 + n2
        print(f'The sum between {n1} and {n2} is : {result}')

    elif count == 2:
        result = n1 * n2
        print(f'The multiplication between {n1} and {n2} is : {result}')

    elif count == 3:

        if n1 > n2:
            print(f'The biggest number is {n1}')
        elif n2 > n1:
            print(f'The biggest number is {n2}')
        else:
            print(f'The number {n1} is equal to the number {n2}')

    elif count == 4:

        n1 = int(input('Insert the first number: '))
        n2 = int(input('Insert the second number: '))

    elif count == 5:
        break
    else:
        print('Wrong value, try again!')

print('The program has been finished!')