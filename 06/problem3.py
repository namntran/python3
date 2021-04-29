#problem3.py - program that checks if there are two "g"s adjacent and prints happy. All g's must be happy.

"""
Function to check if letter g's in a sentence has an adjoining leter 'g'
"""
def searchHappy(sentence):
    # local variable
    letter = 'g'
    # check single letter g
    if len(sentence) == 1 and sentence[0] == letter:
        return False
    # check each letter of sentence, adjust loop range of len(sentence)-1 otherwise IndexError: string index out of range
    for i in range(len(sentence)-1):
        # declare variables to check adjoining characters
        current_character = sentence[i]
        previous_character = sentence[i-1]
        next_character = sentence[i+1]
        # print(current_character, previous_character, next_character) # temporary value for debugging

        # check sentence if letter g has no g neighbours (false condition)
        if current_character == letter and previous_character != letter and next_character != letter:
            return False

        # check last character separately (due to IndexError) if g, and second last character is not g using slice
        if len(sentence) > 1 and sentence[-1] == letter and sentence[-2] != letter:
            return False
    # else string is happy
    return True

# ask for user input
sentence = input('String: ')
print('Happy?:', searchHappy(sentence))