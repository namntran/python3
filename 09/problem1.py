# Adder REPL

# dictionary to store letters of alphabet
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

m = dict()

def in_alphabet(var_name):
    """function to check if character is a letter in alphabet"""
    # for loop to traverse sentence
    for character in var_name:
        # check if character in defined alphabet dictionary
        if character not in alphabet:
            return False
    return True

def is_digit(val):
    """function to check if character is a number"""
    # for loop to travere line by line
    for character in val:
        # check if character in user input is a number using isdigit() method and return boolean value
        if character.isdigit() == False:
            return False
    return True

# var is variable name contains only letters
def get_var(var_name):
    """function to assign variable"""
    if not in_alphabet(var_name):
        print(f"Syntax Error.")
        return
    val = input(f"Enter a value for {var_name}: ")
    if not is_digit(val):
        print(f"Syntax Error.")
        return
    m[var_name] = int(val)

def print_var(var_name):
    """function to print output to terminal"""
    if is_digit(var_name):
        print(f"{var_name}")
        return
    if not in_alphabet(f"{var_name}"):
        print(f"Syntax Error.")
        return
    if var_name not in m:
        print(f"{var_name} is undefined.")
        return
    print(f"{var_name} equals {str(m[var_name])}")

def copy_var(var, val):
    """function description"""
    if not in_alphabet(var):
        print(f"Syntax Error.")
        return
    if is_digit(val):
        m[var] = int(val)
        return
    if val not in m:
        print(f"{val} is undefined.")
        return
    m[var] = m[val]

def add_var(var, val):
    """function description"""
    if not in_alphabet(var):
        print(f"Syntax Error.")
        return
    if is_digit(val):
        m[var] += val
        return
    if not in_alphabet(val):
        print(f"Syntax Error.")
        return

    if val not in m:
        print(f"{val} is undefined.")
        return
    m[var] += m[val]

# print welcome message to terminal
print(f"Welcome to the Adder REPL.")
# sentinel pattern using while loop
while True:
    # ask user to enter string input
    sentence = input(f"??? ")
    # Adder language statement - exit the REPL or terminate the program
    if sentence == 'quit':
        print(f"Goodbye.")
        break

    user_input = sentence.split()

    if len(user_input) == 1:
        print(f"Syntax Error.")

    elif len(user_input) == 2:
        if user_input[0] == 'input':
            # call function
            get_var(user_input[1])
        elif user_input[0] == 'print':
            print_var(user_input[1])
        else:
            print(f"Syntax Error.")

    elif len(user_input) == 3:
        if user_input[1] == 'gets':
            copy_var(user_input[0], user_input[2])
        elif user_input[1] == 'adds':
            add_var(user_input[0], user_input[2])
        else:
            print(f"Syntax Error.")

    else:
        print(f"Syntax Error.")
