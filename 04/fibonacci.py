# Fibonacci sequence is the sum of the two preceding ones e.g. 0 1 1 2 3 5 6
list1 = [] # create an empty list to store numbers
# variables
x = 0
y = 1
count = 0
length = int(input("Enter a positive number: "))
# generate the Fibonacci sequence
while x < length:
	list1.append(x)
	z = x + y
	# Modify values
	x = y
	y = z
	count += 1
# use map function to convert items in list to a string and then join use space ' ' as separator
# print (' '.join(map(str, list1))) # temporary prints all elements horizontally

# for i, e in enumerate(list1, n_elements):
#     print(e) #temporary prints vertically one element per row

# partition list into sub-lists using matrices with a maximum width of 4
matrix = [list1[i:i+4] for i in range(0,len(list1),4)]
for l in matrix:
		# use map function to convert items in list to a string and then join using space ' ' as separator
		print (' '.join(map(str, l)))
