# program that calculate the sum of the first and last integers of two lists
# print the larger sum or tie if same
# prints the sum if the integer by itself

# ask for user input separated by space
list1 = str(input("List 1: "))
list2 = str(input("List 2: "))

# split string into separate characters
list1 = list1.split()
list2 = list2.split()

# convert strings in list to integers using map() function
list1 = list(map(int, list1))
list2 = list(map(int, list2))

# get the first and last integer of each list using slice
# firstlast1 =  list1[::len(list1)-1] # temporary value
# firstlast2 =  list2[::len(list2)-1] # temporary value
# print("first and last element of list 1: ", firstlast1)
# print("first and last element of list 2: ", firstlast2)

# get the first and last integer of list 1 using slice
firstnum1 =  (list1[0])
lastnum1 =  (list1[-1])
# get the first and last integer of list 2 using slice
firstnum2 =  (list2[0])
lastnum2 =  (list2[-1])

totalfirstnum = firstnum1+firstnum2
totallastnum = lastnum1+lastnum2

# print("list 1: ", firstnum1, lastnum1) # temporary value
# print("list 2: ", firstnum2, lastnum2) # temporary value
# print(totalfirstnum, totallastnum) # temporary value

# when there is only one integer in list, the sum is integer itself
if len(list1) == 1:
    print("Output: ", firstnum1)
# when there is only one integer in list, the sum is integer itself
elif len(list2) == 1:
    print("Output: ", firstnum2)
# print the larger sum of the first and last integers of lists
elif totalfirstnum > totallastnum:
    print("Output: ", totalfirstnum)
elif totallastnum > totalfirstnum:
        print("Output: ", totallastnum)
# in the even ot tie, print "Same"
elif totalfirstnum == totallastnum:
    print("Output: Same")
else:
    print("invalid input")
