# prompts for the name of the file to read, then prints number of characters, words, lines

# ask user for file name
path = input("File name: ")
try:
    f = open(path, "r")
    # use 3 counters for loop
    num_characters = 0
    num_words = 0
    num_lines = 0

    for line in f:
        # use split to get list of strings
        words = line.split()

        # use len(str) to get number of character
        num_characters += len(line)
        # use len(str) to get number of words
        num_words += len(words)
        # get number of lines
        num_lines += 1

    print("Characters: ", num_characters, end = "\n")
    print("Words: ", num_words, end = "\n")
    print("Lines: ", num_lines, end = "\n")
    f.close()
except:
    print("Can't read file '", path, "'.", sep ="")