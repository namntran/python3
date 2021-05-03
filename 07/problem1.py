# program that prompts for name of source file to read and target file to write
# copy content  of source file to target file, remove empty lines and count empty lines

source_file = input("Source file: ")
target_file = input("Target file: ")

try:
    file = open(source_file, "r")

except:
    print("Can't read file '", source_file, "'.", sep ="")

if(file):
    line = file.read()
    sentence = line.split('\n')
    empty_lines = len(sentence)
    sentence = [s for s in sentence if s]
    lines_removed = empty_lines - len(sentence)
    # print(sentence) # temporary print statement
    file.close()

file = open(target_file, "w")
for i in sentence:
    file.writelines(i + "\n")

file.close()
print("Lines removed: ", str(lines_removed))