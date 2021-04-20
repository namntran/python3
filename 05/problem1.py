# program that prints the shortest string that was entered, breaks at letter A

#declare variables
sentence = input("Enter a string: ")
shortestString = sentence

#run this while loop until user does not enter "A"
while True:
#Ask user to enter String input
    sentence = input("Enter a string: ")
#check if entered string starts with letter A then break out of loop
    if sentence.startswith("A"):
        break
    # compare the length of sentence to the shortest string
    elif len(sentence) < len(shortestString):
        shortestString = sentence
#Print the shortest string using conversion specifier to convert value to string in quotation marks
print("Shortest string was: ","'%s'" % shortestString)

