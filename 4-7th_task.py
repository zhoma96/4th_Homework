from math import factorial

def factorial_number(n):
    f_num = 1
    if n == 0:
        yield f'{n}! = 1'
    for i in range(1, n + 1):
        f_num *= i
        print(f'{i}! = {f_num}')

for el in factorial_number(int(input('Factorial number: '))):
    print(el)
