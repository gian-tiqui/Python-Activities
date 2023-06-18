# Tiqui, Michael Gian M.
# BSIT - 3D
# Week 13 - Addition Functions


def print_space(n, b=True):
    if b:
        print(' ' * n)
    else:
        print(' ' * n, end='') 
    


def print_equals(n, b=True):
    if b:
        print('=' * n)
    else:
        print('=' * n, end='') 


def get_sum(start, end):
    if start < end:
        return sum(range(start, end + 1))
    elif start > end:
        return sum(range(start, end - 1, -1))
    elif start == 1 and start == 0:
        return start
    else:
        return end


def try_again():
    print('\nDo you want to add new numbers?')
    again = input('Enter \'y\' or \'n\' : ')

    if again.lower() == 'y':
        sum_function()
    elif again.lower() == 'n':
        exit()
    else:
        print("Invalid input.")
        try_again()


def sum_function():
    print()
    print_equals(10, False)
    print(' Addition Program ', end='')
    print_equals(10)
    print()

    first_number = int(input('Enter first number : '))
    last_number = int(input('Enter  last number : '))

    print()
    print_equals(38)
    print_space(2, False)
    print(' Sum of all numbers from {0} to {1}.'.format(first_number, last_number))
    print_equals(38)
    print()
    print_space(15, False)
    if get_sum(first_number, last_number) < 10:
        print('=> {0}  <='.format(get_sum(first_number, last_number)))
    else:
        print('=> {0} <='.format(get_sum(first_number, last_number)))
    print()
    print_equals(38)
    print()
    print_equals(38)
    try_again()

    
sum_function()
