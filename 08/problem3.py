# program to check if list in file is an arithmetic progression and print true or false

def isArithmetic(list):
    """function to check if list is an arithmetic progression"""
    # if list equals to 1 element
    if len(list) == 1:
        # return output
        return True
    else:
        # find the difference for each element in list, subtract the first element from second gap, 3-2, 2-1
        difference = list[1] - list[0]
    # for loop to traverse line by line to check difference between each element
        for i in range(len(list) - 1):
            # difference between two sequential numbers
            if list[i + 1] - list[i] != difference:
                # if difference between elements not equal, return false
                return False
        # if difference between elements are same, return true
        return True

# ask user for file name
path = input("File name: ")
# list to store all the lines to get list of strings
list1 = []
count = 0

# open and read file from user input
with open(path) as file:
    # read lines into list using rstrip() to remove white space
    rows = [row.rstrip() for row in file]
#
#  for loop to traverse line by line and add elements into list
for item in rows:
    # append lines to list, convert to integers
    list1.append([int(number) for number in item.split()])

# for loop to traverse line by line and print output
for item in list1:
    # print each row and call function (boolean = True or False)
    print(rows[count], isArithmetic(item))
    # increment count
    count += 1

# close file
file.close()