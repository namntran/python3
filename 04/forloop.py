num = int(input("enter a positive number: "))

# top of diamond
rows = 2 * num-1 # example 2*3-1 = 5
middleRow = rows//2+1
for i in range(0,middleRow, 1):
    for j in range (0, middleRow-i): # for loop to print empty spaces
        print(" ", end="")
    for k in range(0, 2*i+1): # for loop to print "X"
        print("X", end="")
    print("")

# bottom of diamond
rows = 2 * num-1 # example 2*3-1 = 5
middleRow = rows//2+1
for i in range(rows//2-1, -1, -1):
    for j in range (0, middleRow-i): # for loop to print empty spaces
        print(" ", end="")
    for k in range(0, 2*i+1): # for loop to print "X"
        print("X", end="")
    print("")