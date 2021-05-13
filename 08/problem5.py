	# Each new meeting, you get one new patient infected

	# #at loop 6
	# 	For loop
	# 		List_of_string

	# 		For loop for traversing the name of the list_of_string:

	# 			If name endswith"*"

	# 				Add the name in the list

	# 			# find neighbours and append to infected list [i +1] [i -1]

	# 			Name = check index of name to see if it in infected list, append to infected list

	# Open and read file
	# For loop, use split function to get list of strings
	# Need for loop to traverse file line by line (get meeting number and attendees)
	# 	→ Condition, check last character for asterisk at each name
	# 	→ Put Harry in infected_list[]
	# At loop 6, you have a list of strings, need another variable to record Harry's index

def getInfected(output):
	"""function to find common elements """

# ask user for file name
path = input("File name: ")
# list to store all the lines to get list of strings
list1 = []
count = 0

# open and read file from user input
with open(path) as file:
    # read lines into list using rstrip() to remove white space
    rows = [row.rstrip() for row in file]

#  for loop to traverse line by line and add elements into list
for name in rows:
    # append lines to list
    list1.append([str(names) for names in name.split()])

# for loop to traverse line by line and print output
for name in list1:
    # print each row
    print(rows[count])
    # increment count
    count += 1

# close file
file.close()