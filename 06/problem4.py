# problem4.py
# program that allows the user to enter the marks of 5 students in 4 courses
# output the highest average marks for students and courses

def get_average(list):
    """ function to get average score """
    total = 0
    for i in list:
        total += i
    return total/len(list)

# declare variables
grades = []# list to store grades
students = 5 # rows
courses = 4 # columns
# lists to store grades of different courses
course1 = []
course2 = []
course3 = []
course4 = []
# list to store the average of student marks
highestAverageStudentMarks = []

for i in range(students):
    # ask for user input
    print("Student",i + 1,"(courses 1 - 4): ", end="")
    # separate list of integers from user input and separate
    row = list(map(int, input().split(" ")))
    # add the integers to a list
    grades.append(row)

for students in grades:
    # get the average of the list
    average = get_average(students)
    # add the average of each student into list
    highestAverageStudentMarks.append(average)
# printing the highest average student marks from list
print('The highest average mark of students:', max(highestAverageStudentMarks))

# add grades into different courses (columns)
for courses in grades:
    course1.append(courses[0])
    course2.append(courses[1])
    course3.append(courses[2])
    course4.append(courses[3])

# calculate the average for each course
averageCourse1 = get_average(course1)
averageCourse2 = get_average(course2)
averageCourse3 = get_average(course3)
averageCourse4 = get_average(course4)
# add the average of each course to a list
highestAverageCourseMarks = [averageCourse1, averageCourse2, averageCourse3, averageCourse4]

# print("Course 1 results: ", course1,  "Course 2 results: ", course2,  "Course 3 results: ", course3, "Course 4 results: ", course4) # temporary value for debugging
# print("Average Course 1 results: ", averageCourse1, "Average Course 2 results: ", averageCourse2, "Average Course 3 results: ", averageCourse3, "Average Course 4 results: ", averageCourse4) # temporary value for debugging
# printing the highest average course marks from list
print('The highest average mark of courses: ', max(highestAverageCourseMarks))