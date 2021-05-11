# find the common element in two lists

def getCommonElements(output):
	"""function to find common elements """
	list1_as_set = set(list1) # set() to convert one of the lists to a set
	intersection = list1_as_set.intersection(list2) # call set.intersection() on new set with other list to find common elements
	# need third list to store common elements
	output = list(intersection) # use list(iterable) to convert resultant set of commone elements to a list
	return output

# use while loop to end input blank line
while True:
	# ask user for input string
	list1 = str(input("List 1: "))
	list2 = str(input("List 2: "))
	# check if sentence empty, if so break out of loop
	if len(list1) or len(list2) == 0:
		break

# split string into separate characters
list1 = list1.split()
list2 = list2.split()

# convert strings in list to integers using map() function
list1 = list(map(int, list1))
list2 = list(map(int, list2))

output = 0
# print output and call function
print("Output: ", getCommonElements(output))