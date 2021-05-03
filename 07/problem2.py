# prompts for the name of the file to read
# print the first two lines and last two lines

# ask user for file name
path = input("File name: ")

try:
    f = open(path, "r")
    # list to store all the lines to get list of strings
    lines = []
    # use for loop to traverse file line by line
    for line in f:
        lines.append(line.strip("\n"))

    # print using slice of list
    print(lines[0]) # first line in list
    print(lines[1]) # second line in list
    print(lines[-2]) # second last line in list
    print(lines[-1]) # last line in list

    f.close()
except:
    print("Can't read file '", path, "'.", sep ="")