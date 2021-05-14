# program to find ground zero patient and new patients infected at each meeting

"""function to find if meeting attendees infected """
def isCovid(rows):
    # permanent list to record infections
    infectedList = []
    # for loop to traverse file line by line
    for line in rows:
		# temporary list to record new infections
        newInfected = []
        attendees = line.split()
		# variables needed to record Harry's index in meeting 6
        meetingNumber = attendees[0]
        meetings = attendees[1:]
        index = 0

        for name in meetings:
            # check if the name endswith() method with * for fever (Harry)
            if name.endswith("*"):
                newInfected.append(name.strip("*"))
				# if this person is infected add to temporary list
                newInfected.append(meetings[index-1])
				# check for meeting attendees
                if index == (len(meetings) -1):
                    index = -1
				# append new names to list
                newInfected.append(meetings[index+1])
                # break the loop
                break

            for infected in infectedList:
                if name == infected:
					# if this person is infected add to temporary list
                    newInfected.append(meetings[index-1])
					# check meeting number
                    if index == (len(meetings) -1):
                        index = -1
					# append new names to list
                    newInfected.append(meetings[index+1])
            index+=1
		# add temporary list to permanent list
        infectedList = list(set(infectedList + newInfected))

        if len(infectedList):
            # Print meeting number and names of infected
            print(meetingNumber, " ".join(infectedList), len(infectedList))

# ask user for file name
path = input("File name: ")
# list to store all the lines to get list of strings
list1 = []
covidList = []
count = 0

# open and read file from user input
with open(path) as file:
    # read lines into list using rstrip() to remove white space
    rows = [row.rstrip() for row in file]

#  for loop to traverse line by line and add elements into list
for name in rows:
    # append lines to list
    list1.append([str(names) for names in name.split()])

# for loop to traverse line by line and print output - temporary for debugging
# for name in list1:
#     # print each row
#     print(rows[count])
#     # increment count
#     count += 1

# function is called here
isCovid(rows)

# close file
file.close()