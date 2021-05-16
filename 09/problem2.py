# Adder interpreter that prompts for filename from user and executes files

# dictionary to store letters of alphabet using key: value pairs
alphabet = {
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5',
    'f':'6',
    'g':'7',
    'h':'8',
    'i':'9',
    'j':'10',
    'k':'11',
    'l':'12',
    'm':'13',
    'n':'14',
    'o':'15',
    'p':'16',
    'q':'17',
    'r':'18',
    's':'19',
    't':'20',
    'u':'21',
    'v':'22',
    'w':'23',
    'x':'24',
    'y':'25',
    'z':'26',
}
# dict() function creates an empty dictionary to store and retrieve values
# need empty dictionary with unique keys for every new variable created
lookUpTable = dict()

# function 1
def assign_variable(variable_name):
    """function to prompt user to enter value for variable"""
    # check variable name, call function 5 to check type
    if not in_alphabet(variable_name):
        print(f"Syntax Error.")
        return
    # prompt user to enter a value
    value = input(f"Enter a value for {variable_name}: ")
    # check value type, call function 6 to check type
    if not is_digit(value):
        print(f"Syntax Error.")
        return
    # update dictionary
    lookUpTable[variable_name] = int(value)

# function 2
def print_variable(variable_name):
    """function to print variable name and value"""
    # check variable type, call function 6 to check type
    if is_digit(variable_name):
        print(f"{variable_name}")
        return
    # check variable type, call function 5 to check type
    if not in_alphabet(f"{variable_name}"):
        print(f"Syntax Error.")
        return
    # check variable names in dictionary
    if variable_name not in lookUpTable:
        print(f"{variable_name} is undefined.")
        return
    # print variable names and value
    print(f"{variable_name} equals {str(lookUpTable[variable_name])}")

# function 3
def update_variable(variable, value):
    """function to assign variable to value"""
    # check value type, call function 5 to check type
    if not in_alphabet(variable):
        print(f"Syntax Error.")
        return
    # check value type, call function 6 to check type
    if is_digit(value):
        lookUpTable[variable] = int(value)
        return
    # check value in dictionary
    if value not in lookUpTable:
        print(f"{value} is undefined.")
        return
    # update dictionary
    lookUpTable[variable] = lookUpTable[value]

# function 4
def add_variable(variable, value):
    """function to add value to variable"""
    # check value type, call function 6 to check type
    if is_digit(value):
        lookUpTable[variable] += value
        return
    # check value type, call function 5 to check type
    if not in_alphabet(value):
        print(f"Syntax Error.")
        return
    # check dictionary
    if value not in lookUpTable:
        print(f"{value} is undefined.")
        return
    # update dictionary
    lookUpTable[variable] += lookUpTable[value]

# function 5
def in_alphabet(variable_name):
    """function to check type is letter"""
    # for loop to traverse sentence
    for character in variable_name:
        # check value not in alphabet dictionary
        if character not in alphabet:
            return False
    return True

# function 6
def is_digit(value):
    """function to check type is number"""
    # for loop to traverse line
    for character in value:
        # check value is a number using isdigit() method and return boolean value
        if character.isdigit() == False:
            return False
    return True

# ask user for file name
path = input("Script name: ")
# open the file and read it line by line using readline() method
filename = open(path, 'r')
path = filename.readline()

# declare variables and ask for user input
sons = int(input('Enter a value for sons: '))
daughters = int(input('Enter a value for daughters: '))
# variable to add sum of sons + daughter
sumTotal = sons + daughters
# print output
print(f"children equals {sumTotal}")

# close file
filename.close()