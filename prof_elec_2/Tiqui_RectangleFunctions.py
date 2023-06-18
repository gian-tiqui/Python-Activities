# Tiqui, Michael Gian M.
# BSIT - 3D
# Week 13 - Rectangle Functions


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


def rectangle(m, n):
    for i in range(m):
        print_space(11, False)
        for j in range(n):
            print("*", end='')
        print()


def try_again():
    print('\nDo you want to generate a new rectangle?')
    again = input('Enter \'y\' or \'n\' : ')

    if again.lower() == 'y':
        generate_rectangle()
    elif again.lower() == 'n':
        exit()
    else:
        print("Invalid input.")
        try_again()


def generate_rectangle():
    print()
    print_equals(10, False)
    print(' Rectangle Program ', end='')
    print_equals(10)
    print()

    height = int(input('Enter height of the rectangle : '))
    width = int(input('Enter  width of the rectangle : '))

    print()
    print_equals(39)
    print_space(2, False)
    print('Your rectangle has been generated!')
    print_equals(39)
    print()
    rectangle(height, width)
    print()
    print_equals(39)
    print('  Dimensions => Height: {0}    Width: {1}'.format(height, width))
    print_equals(39)
    try_again()
    
generate_rectangle()
