# Tiqui, Michael Gian M.
# BSIT - 3D
# Week 13 - Merge Functions


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


def merge(lst1, lst2):
    lst1.sort()
    lst1.extend(sorted(lst2))
    return lst1


def try_again():
    print('\nDo you want to merge new lists?')
    again = input('Enter \'y\' or \'n\' : ')

    if again.lower() == 'y':
        merge_function()
    elif again.lower() == 'n':
        exit()
    else:
        print("Invalid input.")
        try_again()


def merge_function():
    print()
    print_equals(35, False)
    print(' Merge Program ', end='')
    print_equals(35)
    print()

    temp_lst1 = input('Enter elements of the 1st list separated by spaces : ')
    temp_lst2 = input('Enter elements of the 2nd list separated by spaces : ')

    lst1, lst2 = temp_lst1.split(), temp_lst2.split()
    
    print()
    print_equals(85)
    print_space(31, False)
    print(' This is the merged list')
    print_equals(85)
    print()
    print(merge(lst1, lst2))
    print()
    print_equals(85)
    print()
    print_equals(85)
    try_again()

    
merge_function()
