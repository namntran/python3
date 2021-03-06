# Given an input number n, print a diamond shape with 2*n-1 rows
"""
Example = 3 (5 rows)
Row1: 4 spaces, 1 star
Row2: 3 spaces, 3 stars
Row3: 2 spaces, 5 stars
Row4: 3 spaces, 3 stars
Row5: 4 spaces, 1 star
"""
num = int(input("enter a positive number: "))


rows = 2 * num-1
middleRow = rows//2 + 1
# top of diamond
for i in range(0,middleRow, 1):
    for j in range (0, middleRow-i): # for loop to print empty spaces
        print(" ", end="")
    for k in range(0, 2*i+1): # for loop to print "X"
        print("X", end="")
    print("")
# bottom of diamond
for i in range(rows//2-1, -1, -1): # start midway, inverse pyramid
    for j in range (0, middleRow-i): # for loop to print empty spaces
        print(" ", end="")
    for k in range(0, 2*i+1): # for loop to print "X"
        print("X", end="")
    print("")