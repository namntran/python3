# program that converts all digits in a string to underline

#Write a function that converts all digits in a string to underline.
def convertDigitsUnderline (sentence):
    """Convert all numbers in a string to underscore."""
    for i in sentence:
        #check if character in user input is a number using isdigit() method, boolean
        if i.isdigit() == True:
            #replace the numbers in string to underline using string replace() method
            sentence = sentence.replace(i, "_")
    return sentence

#ask user to enter String input
sentence = input("Input a string: ")
print (convertDigitsUnderline(sentence))