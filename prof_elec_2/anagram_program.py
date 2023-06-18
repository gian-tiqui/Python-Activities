import time


def conv(string):
    m = {}

    for i in string:
        if i in m.keys():
            m[i] = m[i] + 1
        else:
            m[i] = 1

    return m


def is_anagram(m1, m2):
    return m1 == m2


if __name__ == '__main__':

    space_center, space, line, = 17, 24, 54
    choice = ""

    print("=" * line)
    print("||{0}  {0}||".format(" " * space))
    print("||{0}  {0}||".format(" " * space))
    print("||{0}Anagram Checker {0}||".format(" " * space_center))
    print("||{0}  {0}||".format(" " * space))
    print("||{0}  {0}||".format(" " * space))
    print("=" * line)

    print()
    choice = input("    Do you want to continue? Enter \"Y\" or \"N\" : ")
    print("\n" + "=" * line)

    if choice.lower() == "n":
        print("\tExiting program...")
        exit()
    elif choice.lower() == "y":
        while choice != "n":
            first_word = input("\n\t\tEnter first word   : ")
            second_word = input("\t\tEnter second word  : ")
            print("\n" + "=" * line)

            print("\n\tChecking if these words are anagram....")
            print()

            for i in range(0, 54):
                print("=", end="")
                time.sleep(0.12)

            print("\n||{0}Anagram Checker Result{0}||".format(" " * (space_center - 3)))
            print("=" * line)
            print("\n\tThe words {0} and {1} are anagram!".format(first_word, second_word)
                  if is_anagram(conv(first_word.lower()), conv(second_word.lower()))
                  else "\n\tThe words {0} and {1} aren't anagram.".format(first_word, second_word))

            choice = input("\n\tDo you want to try again? \"Y\" or \"N\" : ")

        print("\n\tExiting program", end="")
        for i in range(5):
            print(".", end="")
            time.sleep(0.5)
        exit()
    else:
        print("\n" + "=" * 50)
        print("||{0}Invalid Input {0}||".format(" " * 16))
        print("=" * 50)
        exit()
