import time


interval = 0.03


def right_triangle():

    row = int(input("\tEnter size : "))

    print("\n\tConstructing your shape...")
    print()

    for ix in range(line):
        print("=", end="")
        time.sleep(interval)

    for i in range(row + 1):
        print("\t", end="")
        for j in range(i):
            print(" * ", end="")
        print()

    print("=" * line)


def inversed_right_triangle():

    row = int(input("\tEnter size : "))

    print("\n\tConstructing your shape...")
    print()

    for ix in range(line):
        print("=", end="")
        time.sleep(interval)

    print()
    
    for i in range(row, 0, -1):
        print("\t", end="")
        for j in range(0, i):
            print(" * ", end="")
        print()

    print("=" * line)


def normal_triangle():

    k = 0
    row = int(input("\tEnter size : "))

    print("\n\tConstructing your shape...")
    print()

    for ix in range(line):
        print("=", end="")
        time.sleep(interval)

    print()
    
    for i in range(1, row + 1):
        for space in range(1, (row - i) + 1):
            print(end="  ")

        while k != (2 * i - 1):
            print("* ", end="")
            k += 1

        k = 0
        print()
        
    print("=" * line)  


def triangle_picker():
    print("=" * line)
    print("||\tChoose from the shapes below:{0}||".format(" " * 18))
    print("||\t1. Right Triangle{0}||".format(" " * 30))
    print("||\t2. Inversed Right Triangle{0}||".format(" " * 21))
    print("||\t3. Normal Triangle{0}||".format(" " * 29))
    
    print("=" * line)

    triangle_choice = int(input("\tEnter number of your choice : "))

    if triangle_choice == 1:
        right_triangle()
    elif triangle_choice == 2:
        inversed_right_triangle()
    elif triangle_choice == 3:
        normal_triangle()
    else:
        print("\tInvalid input.")


def quadrilateral():
    width = int(input("\tEnter width  : "))
    height = int(input("\tEnter height : "))
    print("\n\tConstructing your shape...")
    print()

    for ix in range(line):
        print("=", end="")
        time.sleep(interval)

    print()

    for ix in range(width):
        print("\t", end="")
        for j in range(height):
            print(" * ", end="")
        print()

    print("=" * line)


if __name__ == "__main__":
    line, space = 57, 53

    print("=" * line)
    print("||{}||".format(" " * space))
    print("||{0}Shape Program{0}||".format(" " * ((44 // 2 - len("Shape Program") // 2) + 4)))
    print("||{}||".format(" " * space))
    print("=" * line)

    while True:
        print("=" * line)
        print("||\tChoose from the shapes below:{0}||".format(" " * 18))
        print("||\t1. Quadrilateral{0}||".format(" " * 31))
        print("||\t2. Triangle{0}||".format(" " * 36))
        print("=" * line)

        shape_choice = int(input("\tEnter number of your choice : "))

        if shape_choice == 1:
            quadrilateral()
        elif shape_choice == 2:
            triangle_picker()
        else:
            print("\tInvalid input.")

        choice = input("\tDo you want to try again? Enter \"Y\" or \"N\" : ")

        if choice.lower() == "n":
            break

    print("\n\tExiting program", end="")
    for i in range(5):
        print(".", end="")
        time.sleep(interval)
    
