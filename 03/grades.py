# Write a program that asks the user for a number of marks, and prints the grade awarded

n = int(input("How many marks? "))
if (n >= 85):
    print("7")
elif (n >= 75):
    print("6")
elif (n >= 60):
    print("5")
elif (n >= 50):
    print("4")
else:
    print("F")
