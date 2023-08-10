# Tiqui, Michael Gian M.
# BSIT - 3D
# Week 6 - Wordscapes

# Python Random Module
from random import randint

# Variables to be used in the program
word, score, guesses, guess_num = "concavity", 0, [], 1

# List of messages to be used in the output later
right_messages = ["Nice!", "Good Job!", "Great Work!", "Awesome!", "Good Work!"]
wrong_messages = ["Nice try! but", "Awww", "Sadly", "Please try again"]

# List of strings with slice operators
words = [
    word[0] + word[-3:],  # city
    word[3:],  # cavity
    word[2] + word[4:6] + word[-1],  # navy
    word[:3] + word[-2] + word[4] + word[3:8:4],  # contact
    word[0:4] + word[4:8:3],  # concat
    word[0:2] + word[0:2] + word[4],  # cocoa
    word[0:2] + word[3:5] + word[::-1][2:7:4],  # cocain
    word[3:5] + word[::-1][1:3] + word[1:3],  # cation
    word[3:5] + word[2] + word[::-1][1:3] + word[0],  # cantic
    word[::-1][4:6] + word[::-1][1:3] + word[1:3],  # action
    word[::-1][1:3] + word[2:11:6],  # tiny
    word[::-1][3:5] + word[2:10:4] + word[7:],  # vanity
    word[::-1][2:9:4] + word[::-1][1:10:6],  # into
    word[0:2] + word[4:8:3],  # coat
    word[3::5] + word[::-1][4:7:2],  # cyan
    word[::-1][3:5] + word[::-1][2:7:4],  # vain
    word[::-1][1:8:6] + word[2:8:4] + word[0],  # tonic
    word[4] + word[::-1][1:8:6] + word[2:8:4] + word[0],  # atonic
    word[::-1][6:8] + word[::-1][3:5],  # nova
    word[::-1][2:6:3] + word[1:3],  # icon
    word[0:2] + word[::-1][2:9:4],  # coin
    word[3::5] + word[::-1][4:7:2] + word[1:9:6] + word[::-1][2:9:6],  # cyanotic
    word[3:5] + word[2:8:5],  # cant
    word[::-1][1:5:3] + word[0:2],  # taco
    word[0:2] + word[3:5],  # coca
    word[:3] + word[5:7] + word[3:8:4]  # convict
]

# Printing using formatting methods, repetition operator, special characters
print("=" * 50 + "  Wordscapes  " + "=" * 50)

print("\n\t\t\tWelcome to the Wordscapes game made in Python Programming Language")
print("\t\t     In this game you will guess words that is formed from the word \"{}\"".format(word))
print("\t\t\t     Please enable fullscreen mode to avoid screen glitches")
print("\n\t\t\t\t\t\t   !! RULES !!\n")
print("\t\t\t 1. The game will only end once you reached the score of 10")
print("\t\t\t 2. Else it will continue to ask your guesses")
print("\t\t\t 3. You cannot use the same word you have previously entered.")
print("\t\t\t 4. If you wish to exit, you may do so by typing \"exit\".")
print("\t\t\t 5. You can type in any case")
print("\n" + "=" * 114)

# Input statement if the user wants to continue
choice = input("\n\t\t\t\t Do you want to play? Enter \"Y\" or \"N\" : ")

# If elif else statements
if choice.lower() == "n":
    print("\n\n\t\t\t\t\t   Closing the game...")
elif choice.lower() == "y":

    print("\n" + "=" * 114 + "\n")

    # While loop to limit the score of the user
    while score < 10:

        print("\n\t\tWord: {0}\t\t\t\t\t\t\t\tScore: {1}\n".format(word, score))
        print("\t\tYour guesses: {}\n".format(guesses))

        # Guess input from the user
        guess = input("\t\tEnter your guess number {} : ".format(guess_num))

        # If elif else statements to check user answers
        if guess.lower() == "exit":
            print("\n\t\tExiting the game... Thank you for playing!")
            exit()
        elif guess.lower() == word:
            print("\t\tGetting cheeky eh? but sure")
        elif guess.lower() not in words:
            print("\t\t{0} Your guess \"{1}\" is not formed from the word \"{2}\".".format(
                wrong_messages[randint(0, len(wrong_messages) - 1)], guess, word))
            guess_num += 1
        elif guess.lower() in guesses:
            print("\t\t{0} {1} already exists.".format(wrong_messages[randint(0, len(wrong_messages) - 1)], guess))
            guess_num += 1
        else:
            print("\t\t{0} Your answer \"{1}\" is correct!".format(right_messages[randint(0, len(right_messages) - 1)],
                                                                   guess))
            score += 1
            guess_num += 1
            guesses.append(guess)

    if guess_num == 0:
        print("You exited the game")
    elif 1 < guess_num <= 10:
        print(
            "\n\t\tAmazing! it took you {} guesses to finish the game! You must be a genius. Thank you for playing".format(
                guess_num - 1))
    elif 10 < guess_num <= 20:
        print(
            "\n\t\tGreat Work! it took you {} guesses to finish the game! Splendid indeed. Thank you for playing".format(
                guess_num - 1))
    elif 20 < guess_num <= 30:
        print("\n\t\tNice! it took you {} guesses to finish the game. Keep it up and Thank you for playing".format(
            guess_num - 1))
    elif guess_num > 30:
        print("\n\t\tIt took you {} guesses to finish the game. Thank you for playing".format(guess_num - 1))
    else:
        print("\n\t\tYou finished the game. thank you for playing")

else:
    print("\n\n\t\t\t\t Invalid input. Closing game...")
