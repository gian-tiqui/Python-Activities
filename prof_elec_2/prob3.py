# Tiqui, Michael Gian M.
# IT3D
# Programming problem 3

price_of_meal = float(input("Enter price of meal : "))
tip = int(input("Enter percent tip   : "))

tip_amount = price_of_meal * (tip / 100)
total_bill = tip_amount + price_of_meal

print("\n  ---- ORDER SLIP ----")
print("\nTip Percentage : {0}%".format(tip))
print("Tip amount     : P{0}".format(tip_amount))
print("Total Bill     : P{0}".format(total_bill))
