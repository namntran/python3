# program that prompts for name of source file to read and target file to write
# copy content  of source file to target file, remove empty lines and count empty lines

# ask user for source file name and target file name
source_file = input("Source file: ")
target_file = input("Target file: ")

try:
    # read content of source file
    file = open(source_file, "r")

except:
    print("Can't read file '", source_file, ".", sep ="")

if(file):
    # read file using read() method as an individual string
    line = file.read()
    # split lines using split() method to return list of string separated by new line
    sentence = line.split('\n')
    # use len() method to count the size/ length of list
    total_lines = len(sentence)
    # remove empty lines - list comprehension - don't need append()
    sentence = [i for i in sentence if i]
    # print("print sentence using list comprehension: ", sentence) # temporary print statement for debugging
    # get number of lines removed
    lines_removed = total_lines - len(sentence)
    file.close()

# write content to target file
file = open(target_file, "w")
# traverse file and write to target file
for i in sentence:
    # writelines() method writes the item of list to the target file
    file.writelines(i + "\n")

file.close()
print("Lines removed: ", str(lines_removed))
# print("Total number of lines: ", total_lines) # temporary print statement for debugging