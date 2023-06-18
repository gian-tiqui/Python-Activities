from random import randint

name, player_balance, other_player_bets, player_bets, winning_comb = '', 0, [], [], []

prizes = [500_000_000_000, 500_000, 400_000, 300_000, 200_000]


def generate_rand_nums():
    lst = []
    c = 0

    while c < 6:
        temp = randint(1, 56)
        if temp not in lst:
            lst.append(temp)
            c += 1
        else:
            continue

    return lst


def start_lotto():
    winning_comb = generate_rand_nums()
    other_player_bets = generate_rand_nums()

    print(winning_comb, other_player_bets, sep='\n')

    c = 1

    while c <= 6:
        bet = int(input('enter bet {}: '.format(c)))
        if 1 > bet > 55:
            print('pls enter nums from 1-55')
        elif bet in player_bets:
            print('bet exists.')
        elif bet in other_player_bets:
            print('taken by others.')
        else:
            player_bets.append(bet)
            c += 1


def check():
    money = float(input('Enter money: '))

    if money >= 100:
        age = int(input('Enter age : '))
        if age >= 18:
            name = input('Enter name :')
            start_lotto()
        else:
            print('You are not allowed to play. Goodbye')
            exit()
    else:
        print('You do not have enough money.')
        print('Good bye!')
        exit()


def init_game():
    while True:

        play = input('Do you want to play? : ')

        if play.lower() == 'y':
            check()
        elif play.lower() == 'n':
            print('Okay, see you again!')
            break
        else:
            print('Please enter only y or n.')


init_game()
