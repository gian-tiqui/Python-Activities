# Tiqui, Michael Gian M.
# IT3D
# Programming problem 2

feet = float(input("Enter the value for feet: "))
meters = round((feet * 0.304), 3)
s = "foot" if feet == 1 or feet == float(1) else "feet"

print("{0} {1} is {2} meters.".format(feet, s, meters))

