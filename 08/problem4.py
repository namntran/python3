# program to merge two lists in descending order

"""Function to merge two lists"""
def mergeLists(list1, list2):
	# third list to store variables
    list3 = []
    length1 = len(list1)
    length2 = len(list2)
    i, j = 0, 0

    while i < length1 and j < length2:
		# Check list1[0] and list2[0] for bigger
        if list1[i] > list2[j]:
			# append number to list
            list3.append(list2[j])
			# increment count
            j += 1
        else:
			# append number to list
            list3.append(list1[i])
			# increment count
            i += 1
	# merge lists and return output
    list3 = list3 + list2[j:] + list1[i:]
    return list3

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

# call function to merge two lists from user input
merged_list = mergeLists(list1,list2)
# sort merged list in descending order
merged_list.sort(reverse=True)

# print merged list
print(merged_list)