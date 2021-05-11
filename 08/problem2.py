# find the common element in two lists.

# use while loop to end input blank line
while True:
		# ask user for input string
		list1 = str(input("List 1: "))
		list2 = str(input("List 2: "))
		if len(list1) or len(list2) == 0:
			break

	# split string into separate characters
list1 = list1.split()
list2 = list2.split()

	# convert strings in list to integers using map() function
list1 = list(map(int, list1))
list2 = list(map(int, list2))
	# find common elements of list and set using set.intersection() method
list1_as_set = set(list1) # set() to convert one of the lists to a set
intersection = list1_as_set.intersection(list2) # call set.intersection() on new set with other list to find common elements
# need third list to store common elements
list3 = list(intersection) # use list(iterable) to convert resultant set of commone elements to a list

# print(list1) # temporary print statement for debugging
# print(list2) # temporarty print statement for debugging
print("Output: ", list3)

