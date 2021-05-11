	# Get a list use input
	# Get a string, split and get a list of integers
	# Print original list first
	# Each iteration, remove first element use push. Pop then get 2, 3,4.
	# For i in list, pop index [0]
	# Have a variable for popped number to receive popped element
	# Append popped element at end of list
	# Initial form, length of list = 4 iterations. If length of list = 4, then iterations is 4 loops
#Write a function that converts all digits in a string to underline.
# def rotateList (numbers):
#     """Convert all numbers in a string to underscore."""
#     # for i in sentence:
#     #     #check if character in user input is a number using isdigit() method, boolean
#     #     if i.isdigit() == True:
#     #         #replace the numbers in string to underline using string replace() method
#     #         sentence = sentence.replace(i, "_")
#     return numbers

#ask user to enter String input
# sentence = input("Input a string: ")



list1 = str(input("Input a list: "))

# split string into separate characters
list1 = list1.split()
length = len(list1)

# convert strings in list to integers using map() function
list1 = list(map(int, list1))
print(list1)
# print(len(list1))

# print(list1)
for i in range(length):
	list1.append(list1.pop(0))
	print(list1)
