# program calculates the total trip distance on a grid

# need math library for square root function
import math

# variable to store letters, need to find index of alphabet to convert element in string of letters to int number
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_index(x_value):
    """function to find index of letter in alphabet""" # convert string to int number
    index = 0
    while index < 26: # number of letters in alphabet
        if alphabet[index] == x_value:
            break
        index += 1
    return index

def get_number(y_value):
    """function to get number"""
    index = 0
    for coordinates in y_value:
        # check value is a number using isdigit() method and return boolean value
        if coordinates.isdigit() == True:
            index = index * 10 + int(coordinates)
    return index

def get_distance(destination1, destination2): # example B3, E2, each grid is 0.5 km
    """function to find the distance between two coordinates"""
    # get difference between x values
    a = abs(get_index(destination1[0]) - get_index(destination2[0])) * 0.5 # use abs to ignore negative numbers
    # get difference between y values
    b = abs((get_number(destination1))-(get_number(destination2))) * 0.5 # use abs to ignore negative numbers
    # calculate distance between destination using Pythagoras theorum (a2 + b2 = c2)
    distance = math.sqrt((a)**2 + (b)**2)
    return distance

# ask user for input string of coordinates
coordinates = input("Enter trip map references : ").strip()
# split each coordinate into seperate elements
coordinates = coordinates.split()
distance = 0
index = 0

# use for loop to traverse through user input
for coordinate in coordinates:
    # check for badly formatted map references
    if coordinate[0] not in alphabet and get_number(coordinate) not in range(1,27):
        print("Bad reference : ", coordinate)
        # abort the program if user input error
        exit()

# use while loop to traverse through user input
while index < len(coordinates)-1:
    # calculate total distance between the sum of coordinates
    distance += get_distance(coordinates[index], coordinates[index + 1])
    index += 1
# print distance to 1 decimal place
print("Total Distance = ","%0.1f"%distance, "km")