# program to rotate the numbers so the first number becomes the last
# the rest numbers move one position forward

def rotateNumber():
	"""function to rotate the first and last numbers iteratively """
	# ask for user input
	list1 = str(input("Input a list: "))

	# split string into separate characters
	list1 = list1.split()
	# if length of input list = 4, then iterations is 4 loops
	length = len(list1)

	# convert strings in list to integers using map() function
	list1 = list(map(int, list1))
	# print original list first
	print(list1)

	# each iteration, remove first element by pop() method then repeat for element 2, 3, 4.
	for i in range(length):
		# append popped element at end of list
		list1.append(list1.pop(0))
		print(list1)

# call the function
rotateNumber()