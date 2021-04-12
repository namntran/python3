# program to calculate length and width of room and length of carpet required in whole metres
# carpet.py

import math  # math library to use ceil() function

def required_length(a, b): # define new function with two arguments
    # variables to store user input
    length = max(a,b)
    width = min(a,b)
    # print('length = ', float(length), "m") # temporary - prints only 1 decimal place
    print (f'Length = {length:.3f} m') # f string to specify the precision of float to 3 decimal places
    # print('width = ', float(width), "m") # temporary - prints only 1 decimal place
    print (f'Width = {width:.3f} m') # f string to specify the precision of float to 3 decimal places
    print('Total length required lengthways = ', math.ceil(length), "m")
    print('Total length required widthways = ', math.ceil(width*2), "m")
    print() # print new line for legibility

while True:  # sentinel pattern: while loop
    # variables
    a = float(input('Enter room dimension 1 (m): '))
    b = float(input('Enter room dimension 2 (m): '))

    if a <= 0 or b <= 0:  # exit loop if user enters zero or negative for either dimension
        # print('Enjoy laying carpet') # temporary print statement
        break

    required_length(a, b)  # call new function