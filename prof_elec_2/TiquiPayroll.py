# Tiqui, Michael Gian M.
# BSIT3D
# Programming Problem 5 - Payroll


# Printing multiple # using repetition operator in strings.
print("#" * 33)
print("\n" + " " * 2 + "=" * 6 + " PAYROLL SYSTEM " + "=" * 6 + "\n")
print("#" * 33)

# Getting data from the user using input and type casting.
employee_num = int(input("\nEnter employee number : "))
lname = input("Enter last name       : ")
fname = input("Enter first name      : ")
age = int(input("Enter age             : "))
dep = input("Enter Department      : ")
rate_hour = float(input("Enter Rate per hour   : "))
hours_worked = int(input("Enter Hours Worked    : "))

# Calculating the value of GROSSPAY.
gross_pay = rate_hour * hours_worked

# Printing the entered data of the user using different formatting methods.
print("\n" + "=" * 12 + " PAYSLIP " + "=" * 12)
print("\nEmployee num          : {0}".format(employee_num))
print("Name                  : {0}".format(fname + " " + lname))
print("Age                   : {0}".format(age))
print("Department            : %s" % (dep))
print("Rate                  : {0}".format(round(rate_hour,2)))
print("Hours                 : %d" % (hours_worked))

print("\n" + "=" * 11 + " DEDUCTIONS " + "=" * 10)

# Calculating the values of deductions.
SSS, PagIbig, PhilHealth, TAX = gross_pay * 0.03, gross_pay * 0.04, gross_pay * 0.02, 2085.05

# Printing the deductions using different formatting methods.
print("\nSSS        (3%)       : {0}".format(round(SSS, 2)))
print("PagIbig    (4%)       : {0}".format(round(PagIbig, 2)))
print("PhilHealth (2%)       : {0}".format(round(PhilHealth, 2)))
print("TAX                   : {0}".format(round(TAX, 2)))

# Calculating the value of NETPAY.
net_pay = gross_pay - (SSS + PagIbig + PhilHealth + TAX)

# Printing the results of GROSSPAY, TOTAL DEDUCTIONS, and NETPAY.
print(f"\nGROSSPAY              : {round(gross_pay, 2)}")
print(f"\nTOTAL DEDUCTIONS      : {round(SSS + PagIbig + PhilHealth + TAX, 2)}")
print(f"\nNETPAY                : {round(net_pay, 2)}")

