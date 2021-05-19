from itertools import count, cycle

print('Autogeneration, for quiting type "q"')
for num in count(int(input('1st number: '))):
    print(num, end='')
    quit = input()
    if quit == 'q':
        break

print('Copying your elements and printing, for quiting type "q"')
my_list = input('Input element with space: ').split()
iter_ = cycle(my_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()