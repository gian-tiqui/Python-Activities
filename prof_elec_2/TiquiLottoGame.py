# Tiqui, Michael Gian M.
# BSIT - 3D
# Week 10 - 6/55 Lotto Game

from random import randint
from time import sleep

play = "y"
prizes = [500_000_000.00, 500000.00, 400000.00, 300000.00, 200000.00]

print("=" * 54)
print("||{0}||".format(" " * 50))
print("||{0}Welcome to the lotto!{1}||".format(" " * 14, " " * 15))
print("||{0}||".format(" " * 50))
print("=" * 54)
print("||{0}RULES{1}||".format(" " * 22, " " * 23))
print("=" * 54)
print("||{0}||".format(" " * 50))
print("||{0}1. You must be 18 or above.{1}||".format(" " * 2, " " * 21))
print("||{0}2. You have 6 chances to choose your bets{1}||".format(" " * 2, " " * 7))
print("||{0}3. You are allowed to change your bets.{1}||".format(" " * 2, " " * 9))
print("||{0}4. You are allowed to play more than once.{1}||".format(" " * 2, " " * 6))
print("||{0}5. You need to pay P100 to participate.{1}||".format(" " * 2, " " * 9))
print("||{0}6. Not all of the numbers will be available -{1}||".format(" " * 2, " " * 3))
print("||{0}   - because other players have picked it{1}||".format(" " * 2, " " * 7))
print("||{0}7. You will win the corresponding prices - {1}||".format(" " * 2, " " * 5))
print("||{0}   - depending on how many right bets you have  {1}||".format(" " * 2, ""))
print("||{0}||".format(" " * 50))
print("=" * 54)
print("||{0}PRIZE POOL{1}||".format(" " * 19, " " * 21))
print("=" * 54)
print("||{0}||".format(" " * 50))
print("||{0}JACKPOT   : {2}{1}||".format(" " * 6, " " * 21, prizes[0]))
print("||{0}5 Matches : {2}{1}||".format(" " * 6, " " * 24, prizes[1]))
print("||{0}4 Matches : {2}{1}||".format(" " * 6, " " * 24, prizes[2]))
print("||{0}3 Matches : {2}{1}||".format(" " * 6, " " * 24, prizes[3]))
print("||{0}2 Matches : {2}{1}||".format(" " * 6, " " * 24, prizes[4]))
print("||{0}1 Match   : Balik taya{1}||".format(" " * 6, " " * 22))
print("||{0}0 Match   : You lose{1}||".format(" " * 6, " " * 24))
print("||{0}||".format(" " * 50))

print("=" * 54)
enter_i = input("\n\tDo you want to join? Enter \"y\" or \"n\" : ")

if enter_i.lower() == "y":

    while play.lower() == "y":

        print("\n" + "=" * 54)

        message = "Please answer the questions below..."

        yes = True

        for i in message:
            if yes:
                print("\n\t" + i, end="")
                yes = False
            else:
                print(i, end="")
                sleep(0.02)

        age_verification = input("  \n\n\tAre you 18 or above? Enter \"y\" or \"n\" : ")

        if age_verification.lower() == 'y':

            money = float(input("  \n\tHow much money do you have?           : "))

            while play.lower() == "y":

                if money >= 100:
                    payment_confirmation = input("  \n\tPay P100 to play? Enter \"y\" or \"n\"    : ")

                    if payment_confirmation.lower() == 'y':
                        money -= 100

                        print("\n" + "=" * 54)

                        name = input("  \n\tEnter your name (Optional) : ")

                        bets, winning_nums, other_bets = [], [], []
                        score, counter, counter2, counter3 = 0, 1, 0, 0
                        other_bets_len = [3, 6, 9]

                        while counter3 < 9:
                            temp = randint(1, 55)
                            if temp in other_bets:
                                counter3 -= 1
                            else:
                                other_bets.append(temp)
                                counter3 += 1

                        if name == "" or name is None:
                            name = "Guest"

                        while len(winning_nums) < 6:
                            temp2 = randint(1, 55)
                            if temp2 in winning_nums:
                                counter2 -= 1
                            else:
                                winning_nums.append(temp2)
                                counter2 += 1

                        # Comment to hide
                        print("\tWinning numbers:", winning_nums)

                        confirm_bets = "n"

                        while confirm_bets == "n":

                            print("\n" + "=" * 54)
                            print("  \n\t\t     TAKEN BETS")

                            start2, last2 = 0, 3

                            for i in range(3):
                                print("  \n\t\t      ", end="")
                                for j in range(start2, last2):
                                    if other_bets[j] < 10:
                                        print(other_bets[j], end="  ")
                                    else:
                                        print(other_bets[j], end=" ")
                                print()
                                start2 = last2
                                last2 += 3

                            print("\n" + "=" * 54)

                            while counter <= 6:

                                inp = int(input("  \n\tEnter bet number {}: ".format(counter)))

                                if inp <= 0 or inp > 55:
                                    print("  \n\tPlease enter numbers from 1 - 55 only.")
                                elif inp in bets:
                                    print("  \n\tYou picked this earlier. Please enter another bet")
                                elif inp in other_bets:
                                    print("  \n\tThis number has been taken by other players.")
                                else:
                                    bets.append(inp)
                                    counter += 1

                            print("\n" + "=" * 54)
                            
                            print("  \n\t\t     {0} BETS".format(name.upper() + "'S"))

                            start3, last3 = 0, 3

                            for i in range(2):
                                print("  \n\t\t      ", end="")
                                for j in range(start3, last3):
                                    if bets[j] < 10:
                                        print(bets[j], end="  ")
                                    else:
                                        print(bets[j], end=" ")
                                print("\n")
                                start3 = last3
                                last3 += 3

                            print("=" * 54)

                            print("  \n\tDo you want to continue with the bets?")
                            confirm_bets = input("  \n\tEnter \"y\" or \"n\" : ")

                            if confirm_bets == "n":
                                bets.clear()
                                counter = 1

                        print("  \n\tEvaluating your bets...\n")

                        for i in range(6):
                            if bets[i] in winning_nums:
                                score += 1
                            if bets[i] < 10:
                                print("   \t{0}  : {1}".format(bets[i], "matched" if bets[i] in winning_nums else "not matched"))
                            else:
                                print("   \t{0} : {1}".format(bets[i], "matched" if bets[i] in winning_nums else "not matched"))

                        if score == 6:
                            print("  \n\tCongrats {0} you won a JACKPOT!".format(name))
                            money += prizes[0]
                        elif score == 5:
                            print("  \n\tCongrats {0} you won P{1}!".format(name, prizes[1]))
                            money += prizes[1]
                        elif score == 4:
                            print("  \n\tCongrats {0} you won P{1}!".format(name, prizes[2]))
                            money += prizes[2]
                        elif score == 3:
                            print("  \n\tCongrats {0} you won P{1}!".format(name, prizes[3]))
                            money += prizes[3]
                        elif score == 2:
                            print("  \n\tCongrats {0} you won P{1}!".format(name, prizes[4]))
                            money += prizes[4]
                        elif score == 1:
                            print("  \n\tYou will get your money back.")
                            money += 100
                        else:
                            print("  \n\tSorry you lost...")

                        if money < 100:
                            print("  \n\tSeems like you ran out of money.")
                            print("  \n\tComeback again and thank you for playing!")
                            exit()
                        else:
                            print("  \n\tYour money is now {0}".format(money))

                            play = input("  \n\tDo you want to play again? Enter \"y\" or \"n\" : ")

                    else:
                        print("  \n\tOkay, Good bye.")
                        exit()

                else:
                    print("  \n\tSorry, you do not have enough money to play.")
                    exit()

        elif age_verification.lower() == "n":
            print("\n\tApologies, you are not allowed to play.")
            break
        else:
            print("\n\tPlease enter \"y\" or \"n\" only")
elif enter_i.lower() == "n":
    print("\n\tThank you and good bye!")
    exit()
else:
    print("\n\tInvalid input.")
    print("\n\tPlease enter \"y\" or \"n\" only next time.")
    exit()

print("\n\tThank you and good bye!")
