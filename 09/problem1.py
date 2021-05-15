# Adder REPL has following statements
# quit
# input (prompt user for variable)
# gets (assigns value to variable)
# adds (adds value to variable)
# var is a string that only has letters and no digits
# val is letters or digits

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

def in_alphabet(variable_name):
    """function to check type is letter"""
    # for loop to traverse sentence
    for character in variable_name:
        # check if character in defined alphabet dictionary
        if character not in alphabet:
            return False
    return True

def is_digit(value):
    """function to check type is number"""
    # for loop to travere line by line
    for character in value:
        # check if character in user input is a number using isdigit() method and return boolean value
        if character.isdigit() == False:
            return False
    return True

def assign_variable(variable_name):
    """function to assign value to variable name in dictionary"""
    if not in_alphabet(variable_name):
        print(f"Syntax Error.")
        return
    value = input(f"Enter a value for {variable_name}: ")
    if not is_digit(value):
        print(f"Syntax Error.")
        return
    # update dictionary
    lookUpTable[variable_name] = int(value)

def update_variable(variable, value):
    """function to assign variable to value in dictionary"""
    if not in_alphabet(variable):
        print(f"Syntax Error.")
        return
    if is_digit(value):
        lookUpTable[variable] = int(value)
        return
    if value not in lookUpTable:
        print(f"{value} is undefined.")
        return
    # update dictionary
    lookUpTable[variable] = lookUpTable[value]

def add_variable(variable, value):
    """function to add value to variable in dictionary"""
    if not in_alphabet(variable):
        print(f"Syntax Error.")
        return
    if is_digit(value):
        lookUpTable[variable] += value
        return
    if not in_alphabet(value):
        print(f"Syntax Error.")
        return
    if value not in lookUpTable:
        print(f"{value} is undefined.")
        return
    # update dictionary
    lookUpTable[variable] += lookUpTable[value]

def print_var(variable_name):
    """function to calculate variable name and value"""
    if is_digit(variable_name):
        print(f"{variable_name}")
        return
    if not in_alphabet(f"{variable_name}"):
        print(f"Syntax Error.")
        return
    if variable_name not in lookUpTable:
        print(f"{variable_name} is undefined.")
        return
    # print variable names and value
    print(f"{variable_name} equals {str(lookUpTable[variable_name])}")

# print welcome message
print(f"Welcome to the Adder REPL.")
# sentinel pattern using while loop
while True:
    # ask user to enter string input
    sentence = input(f"??? ")
    # Adder language statement - exit the REPL or terminate the program
    if sentence == 'quit':
        print(f"Goodbye.")
        break

    # split string using split() method
    user_input = sentence.split()

    # if length of sentence equals to 1, then print error message
    if len(user_input) == 1:
        print(f"Syntax Error.")

    # if length of sentence equals to 2, then first user input is "input" or "print"
    elif len(user_input) == 2:
        if user_input[0] == "input":
            assign_variable(user_input[1])
        elif user_input[0] == "print":
            print_var(user_input[1])
        else:
            print(f"Syntax Error.")

    # if length of sentence equals to 3, second user input is "add" or "gets"
    elif len(user_input) == 3:
        if user_input[1] == "gets":
            update_variable(user_input[0], user_input[2])
        elif user_input[1] == "adds":
            add_variable(user_input[0], user_input[2])
        else:
            print(f"Syntax Error.")

    else:
        print(f"Syntax Error.")