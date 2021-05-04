# program that prompts for the name of a file
# prints the average of each line

def get_average(list):
    """ function to get average score """
    total = 0
    for i in list:
        total += i
    return total/len(list)

# ask user for file name
path = input("File name: ")

try:
    f = open(path, "r")
    # list to store all the lines to get list of strings
    scores = []
    grades = []

    # use for loop to traverse file line by line
    for line in f:
        # append lines to list
        scores.append(line.strip("\n"))
        # separate list of integers from user input and separate
        row = list(map(int, line.split(" ")))
        # # # add the integers to a list
        grades.append(row)

    # compute average number in each line using index
    course1 = get_average(grades[0])
    course2 = get_average(grades[1])
    course3 = get_average(grades[2])
    course4 = get_average(grades[3])
    # print("sum grades 1:", sum_grades1)

    # print output for lines 1, 2, 3, 4
    print("The average of line 1 is", course1)
    print("The average of line 2 is", course2)
    print("The average of line 3 is", course3)
    print("The average of line 4 is", course4)

    # # temporary print statements for debugging
    # print("list of strings line 1: ", scores[0])
    # print("list of strings line 2: ", scores[1])
    # print("list of strings line 3: ", scores[2])
    # print("list of strings line 4: ", scores[3])
    # # temporary print statements for debugging
    # print("list of ints line 1: ", grades[0])
    # print("list of ints line 2: ", grades[1])
    # print("list of ints line 3: ", grades[2])
    # print("list of ints line 4: ", grades[3])
    sum_grades1 = sum(grades[0])

    f.close()
except:
    print("Can't read file '", path, "'.", sep ="")