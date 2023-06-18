# Tiqui, Michael Gian M.
# BSIT - 3D
# Week 5 - Laboratory Exercise

# I initialized the size to be 150 for it to be the amount of "=" for each problem. Also it can be changed if we want -
# - to resize the line which is made of "=".
size = 150

# I used repetition and special characters like \t, \n in the start of every items -
# - to seperate the outputs for each problem.

# 1. if statement sample program

print("\n" + "=" * size + "\n\n\t\t\t\t\t\t\t1. if statement sample program\n\n" + "=" * size)

# For this problem I used a list and dictionary to store random values.
lst = [1, 2, 3, 4, 5]
dictionary = {
    1: "one",
    "two": [5, 4, 3, 2, 1],
    3: 333,
    "four": False,
    5: None
}

print("\nMessage: In this program I will only use the type of the lst and the type of the value in the dictionary "
      "with the key \"two\" and compare them.\n")

# In this line, I compared the type of list and the value of the dictionary with the index "two"
if type(lst) == type(dictionary.get("two")):
    # Since the if statement will return true, it will create a new value with the key of 6 and will store the string -
    # - below and print the string.
    dictionary[6] = "The type of lst (list) is equal to the type of the value {0} in the dictionary with the key of " \
                    "\"two\".".format(
        dictionary.get("two"))
    # I accessed the value of the dictionary by using the elements that is stored in the only list in the dictionary
    print("Result : {}".format(dictionary.get(dictionary.get("two")[0] + dictionary.get("two")[-1])))

# In this line, I inversed the condition in line 19 to negate the condition. Since it will return false, it will not -
# - create a new value
if type(lst) != type(dictionary.get("two")):
    # But if we change the key in the get method in the dictionary to other keys, it will create a new value in the -
    # - dictionary and it will also print the string
    dictionary[7] = "The type of lst (list) is not equal to the type of the value {0} in the dictionary with the key " \
                    "of \"two\".".format(
        dictionary.get("two"))
    # Here I also accessed the value of the dictionary by using the elements that is stored in the only list in the -
    # - dictionary
    print("Result : {}".format(dictionary.get(dictionary.get("two")[0] + dictionary.get("two")[-2])))

# Also if none of the two conditions above are satisfied, it will print nothing.

# 2. if else statement sample program

print("\n" + "=" * size + "\n\n\t\t\t\t\t\t\t2. if else program statement sample\n\n" + "=" * size)

# In this problem, I will use 1 string which will be checked through if and else statements.
string_two = "thisismystring"

# In this line, I printed the messages using format method.
print("\nMessage: In this program, I will use just 1 string that contains \"{}\".".format(string_two))
print("\n" + "=" * 24 + " String Size Checker Result " + "=" * 23)

# This statement will check if the length of the string is greater than 10
if len(string_two) > 10:
    # If it is greater than 10, it will print this line.
    print("\nThe string passed! The string \"{}\" has more than 10 characters.".format(string_two))
else:
    # Else it will print this line.
    print("\nThe string failed. The string \"{}\" has less than 10 characters.".format(string_two))

print("\n" + "=" * 75)

# 3. if elif else statement sample program

print("\n" + "=" * size + "\n\n\t\t\t\t\t\t\t3. if elif else statement sample program\n\n" + "=" * size)

# In this problem, I initialized choice as 2.
choice = 2

# I printed the choices of the games I want to play
print("\nMessage: Please enter a game you want to play.\n")
print("Games:")
print("1. Pokemon Violet")
print("2. Pokemon Legends: Arceus")
print("3. Pokemon: Lets Go, Pikachu")
print("4. Pokemon Sword")
print("5. Pokemon Ultra Sun")
print("6. Pokemon Sun")

# I printed this using formatting method.
print("\nYou entered {}.\n".format(choice))

# I used if elif else statements that will check what the user wants to play. Once the input is changed to less than 0
# or greater than 6, It will output "You are playing nothing", else it will output that you are playing a game.
if choice == 1:
    print("You are playing Pokemon Violet.")
elif choice == 2:
    print("You are playing Pokemon Legends: Arceus")
elif choice == 3:
    print("You are playing Pokemon: Lets Go, Pikachu")
elif choice == 4:
    print("You are playing Pokemon Sword")
elif choice == 5:
    print("You are playing Pokemon Ultra Sun")
elif choice == 6:
    print("You are playing Pokemon Sun")
else:
    print("You are playing nothing")

# 4. Nested if statement sample program

print("\n" + "=" * size + "\n\n\t\t\t\t\t\t\t4. Nested if else statement\n\n" + "=" * size)

# In this problem, I initialized a list of usernames and a username that will be evaluated
usernames, username = ["gian_tiqui", "giannnnn", "sarapchicken"], "giangian"

# I printed this message using formating method and passed the list of usernames.
print("\nMessage: These are the list of the current usernames in the database. \nList: {0}".format(usernames))

# I also printed this message using formating method but I passed the username.
print("\nMessage: Now we will check if the username \"{}\" will pass the tests and will be added to the database.\n".format(
    username
))

print("=" * 21 + " Result " + "=" * 21 + "\n")

# This will check if the length of the username is greater than 7.
if len(username) > 7:
    print("Test 1 passed.")
    # This will check if the user name is not in the usernames.
    if username not in usernames:
        print("Test 2 passed.")
        # This will check if the size of the username is less than 10,000
        if len(usernames) < 10000:
            print("Test 3 passed.")
            # This will add the username to the usernames if it has passed the test
            usernames.append(username)
            print("\nMessage: Your username is added to the usernames.")
        else:
            print("Test 3 failed.\nYour username did not meet one requirement.")
    else:
        print("Test 2 failed.\nYour username did not meet one requirement.")
else:
    print("Test 1 failed. \nYour username did not meet one requirement.")

print("\n" + "=" * 50)

# I printed this message using formatting method and passed the current elements of the list.
print("\nMessage: This is the list of the current usernames.\nList:{}".format(usernames))

# 5. Reverse a string sample program

print("\n" + "=" * size + "\n\n\t\t\t\t\t\t\t5. Reverse a string sample program\n\n" + "=" * size)

# In this problem, I initialized a string that contains my name.
string_five = "Michael Gian M. Tiqui"

# I printed the input to view the string
print("\nOriginal String  : %s" % string_five)
# Then I reversed the string using slice.
print("Reversed String  : {}".format(string_five[::-1]))

# 6. Palindrome sample program

print("\n" + "=" * size + "\n\n\t\t\t\t\t\t\t6. Palindrome sample program\n\n" + "=" * size)

# In this problem, I will use a list that contains different strings.
strings_six = ["Girafarig", "Skeledirge", "o", "Wow", "Pokeball"]

# I used format method to pass the value to the braces in the string.
print("\nMessage: These are the elements of the list: {}".format(strings_six))

# Then I will check if each element is palindrome.
print("\n" + "=" * 5 + " Palindrome checker results " + "=" * 5 + "\n")

# Then I will print the results using format method
# I used the lower method because the the strings contains capital letters.
# I also used ternary operator to print Passed or Failed if depending on the condition
# Lastly, I will compare each values to their reversed values using slice method.
print("{0}  : {1}".format(strings_six[0], "Passed" if strings_six[0].lower() == strings_six[0][::-1].lower() else "Failed"))
print("{0} : {1}".format(strings_six[1], "Passed" if strings_six[1].lower() == strings_six[1][::-1].lower() else "Failed"))
print("{0}          : {1}".format(strings_six[2], "Passed" if strings_six[2].lower() == strings_six[2][::-1].lower() else "Failed"))
print("{0}        : {1}".format(strings_six[3], "Passed" if strings_six[3].lower() == strings_six[3][::-1].lower() else "Failed"))
print("{0}   : {1}".format(strings_six[4], "Passed" if strings_six[4].lower() == strings_six[4][::-1].lower() else "Failed"))

print("\n" + "=" * 39)
