# Fibonacci sequence is the sum of the two preceding ones e.g. 0 1 1 2 3 5 6

list1 = [] # create an empty list to store numbers
# variables
x = 0
y = 1
count = 0
length = int(input("Enter a positive number: "))
# generate the Fibonacci sequence
while x < length:
	# print(x, end = "\n") # temp
	list1.append(x)
	z = x + y
	# Modify values
	x = y
	y = z
	count += 1
#use map function to convert items in list to a string and then join use space ' ' as separator
print (' '.join(map(str, list1)))


