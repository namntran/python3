# Program to sort alphabetically the words form a string provided by the user
def sortLexographic(sentence):
    """function that sorts lexographically"""
    # breakdown string into a list of words in lower case
    words = [word.lower() for word in sentence.split()]
    # sort the list into descending order lexographically
    words.sort(reverse=True)
    # display output of sorted string
    for word in words:
        print(word, end = " ")

# run this loop until user enters empty string
while True:
    # ask user for string input
    sentence = str(input("\nEnter a string: "))
    # call function to display output
    sortLexographic(sentence)
    # check if sentence empty, if so break out of loop
    if len(sentence) == 0:
        break