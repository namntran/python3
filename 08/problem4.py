	# Two lists in random order
	# Allowed to have duplicate lists
	# Need a third list
	# You can use append and sort function to sort lists respectively
	# When to update i, when to update j

	# L1 = [2,4,13,6,3]
	# L2 = [23,4,5,1,7]

	# Sort L1 in descending order
	# L1 =[13, 6, 4, 3, 2
	# L2 = [23, 7, 5, 4, 1]
	# L3 = [23, 13, 7, ],
	# i = 0
	# j = 0
	# 			j += 1
	# 			i + = 1
	# 	If L1[i] > L2[i]
	# 		appendL2
	# I = 0 0 1 1 2 2
	# J = 0 1 1 2 2 3
	# While loop:
	# 	When reach end off

	# l,j = 0
	# Check L,J
	# 	Check L1[0] and L2[0] for bigger

# def merge(list1, list2):
#     res = list1 + list2
#     res.sort()
#     return res

# l1 = [1,2,3]
# l2 = [4,5,6,7]
# print(merge(l1,l2))

# Answer b)

def mergeLists(list1, list2):
    list3 = []
    length1 = len(list1)
    length2 = len(list2)
    i, j = 0, 0
	# If L1[i] > L2[i]
	# 		appendL2
    while i < length1 and j < length2:
        if list1[i] > list2[j]:
            list3.append(list2[j])
            j += 1
        else:
            list3.append(list1[i])
            i += 1
    list3 = list3 + list2[j:] + list1[i:]
    return list3

# l1 = [1,3,3,6]
# l2 = [1,4,5]
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
# call function to merge two lists in ascending order
merged_list = mergeLists(list1,list2)
# sort merged list in descending order
merged_list.sort(reverse=True)
# print out of merged list
print(merged_list)
# print(merge(l1,l2))

