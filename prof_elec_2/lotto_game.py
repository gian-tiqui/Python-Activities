from random import randint

money = 0.0


def display_nums(lst):
    start, last = 0, 3

    for i in range(2):
        print("  \n\t\t      ", end="")
        for j in range(start, last):
            if lst[j] < 10:
                print(lst[j], end="  ")
            else:
                print(lst[j], end=" ")
        print("\n")
        start = last
        last += 3


def generate_other_bets_without(this_bets):
    lst = []
    counter = 0

    while counter < 6:
        random_temp = randint(1, 55)
        if random_temp not in this_bets:
            lst.append(random_temp)
            counter += 1

    return lst


def generate_winning_combinations():
    lst = []
    counter = 0

    while counter < 6:
        random_temp = randint(1, 55)
        if random_temp not in lst:
            lst.append(random_temp)
            counter += 1

    return lst


def exit_game():
    print('Goodbye')
    exit()


def start_game():
    player_bets = []
    winning_combinations = generate_winning_combinations()
    other_player_bets = generate_other_bets_without(winning_combinations)
    prizes = [0, 200_000, 300_000, 400_000, 500_000, 500_000_000]
    counter, score = 1, 0
    global money

    print("winning combination:")
    display_nums(winning_combinations)
    print('taken bets:')
    display_nums(other_player_bets)

    while counter <= 6:

        bet = 0
        not_passed = True

        while not_passed:
            try:
                bet = int(input('Enter bet number {c} : '.format(c=counter)))
            except ValueError:
                print('Please a enter number only.')
            else:
                not_passed = False

        if bet in player_bets:
            print('You entered this number already.')
        elif not (0 < bet <= 55):
            print('Please enter a number from 1 - 55 only.')
        elif bet in other_player_bets:
            print('This has been taken by other players.')
        else:
            player_bets.append(bet)
            counter += 1

    for i in player_bets:
        if i in winning_combinations:
            score += 1

    prize = 0.0

    if score == 1:
        print('Balik taya')
        start_game()
    elif score > 1:
        prize = prizes[score - 1]
    else:
        print('Sorry you lost.')

    print('Congrats! you won {prize_p}!'.format(prize_p=prize))

    money += prize

    print(money)

    if money < 100:
        print('You ran out of money.')
        exit_game()
    else:
        while True:
            play_again = input('Do you want to play again? \'y\' or \'n\' : ')

            if play_again.lower() == 'y':
                money -= 100
                start_game()
            elif play_again.lower() == 'n':
                exit_game()
            else:
                print('Enter only \'y\' or \'n\'.')


def lotto_game():
    global money

    money = float(input('Enter your money : '))

    if money >= 100:
        play = input('Do you want to play? enter \'y\' or \'n\' : ')

        while True:
            if play.lower() == 'y':
                money -= 100
                start_game()
                break
            elif play.lower() == 'n':
                exit_game()
            else:
                play = input('Enter only \'y\' or \'n\' : ')
    else:
        print('You need 100 petot')


def rectangle(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end='')
        print()


def get_sum(start, end):
    return sum(range(start, end + 1))


def merge_sorted(lst1, lst2):
    lst1.extend(lst2)
    return sorted(lst1)


def merge_unsorted(lst1, lst2):
    lst1.sort()
    lst1.extend(sorted(lst2))
    return lst1

