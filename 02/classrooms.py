# program to calculate classrooms for student exams

classSize = 25
bigRoom = int(input("How many big classrooms? "))
smallRoom = int(input("How many small classrooms? "))
students = ((bigRoom*45)+(smallRoom*22))
totalNum = students//classSize
print("Number of classes = ", totalNum)