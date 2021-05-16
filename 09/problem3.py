#program calculates the total trip distance

# store 2D coordinates in tuples
# xs = [C, B, Y]
# ys = [2, 5, 25]

# import math
# trips = input("Enter trip map references: ").strip()
# trips = trips.split(' ')
# bad = False
# for item in trips:
#     if((item[:1]).isalpha() == (item[:1]).isupper() == (item[1:]).isdigit() == True):
#         pass
#     else:
#         print("Bad reference:",item)
#         bad =True
# if(not bad):
#     distance = 0
#     for i in range(len(trips)-1):
#         d1 = ord(trips[i+1][:1]) - ord(trips[i][:1])
#         d2 = int(trips[i+1][1:]) - int(trips[i][1:])
#         distance += math.sqrt(d1**2 + d2**2) * 0.5
#     print("Total distance =","%0.1f"%distance,"km")


import math

# variables to store coordinates from user input
digits = "0123456789"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_index(x_value):
    """function to find index of letter in alphabet"""
    index = 0
    while index  < 26:
        if letters[index] == x_value:
            break
        index += 1
    return index + 1

def get_number(y_value):
    """function to convert string to integer number"""
    number = 0
    for coordinates in y_value:
        if coordinates in digits:
            number = number * 10 + int(coordinates)
    return number

def get_distance(s1, s2):
    """function to find the distance between two coordinates"""
    n1 = get_number(s1)
    n2 = get_number(s2)
    # get length of each triangle
    a = abs(get_index(s1[0]) - get_index(s2[0])) * 0.5
    b = abs(n1-n2) * 0.5
    # distance = pythagoras theorum is a2 + b2 = c2
    distance = math.sqrt((a)**2 + (b)**2)
    return distance

# ask user for input string of coordinates
coordinates = input("Enter trip map references : ").strip()
# split each coordinate into seperate elements
coordinates = coordinates.split()
distance = 0
count = 0

for coordinate in coordinates:
    # check for badly formatted map references
    if coordinate[0] not in letters and get_number(coordinate) not in range(1,27):
        print("Bad reference : ", coordinate)
        # abort the program if user input error
        exit()

while count<len(coordinates)-1:
    # call function
    distance += get_distance(coordinates[count], coordinates[count+1])
    count += 1
# print distance to 1 decimal place
print("Total Distance = ","%0.1f"%distance, "km")