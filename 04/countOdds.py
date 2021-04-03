# program to count even numbers and poisitive numbers

# import statistics # to call median module. Return the median (middle value) of numeric data, using the common “mean of middle two” method.

list1 = [] # create an empty list to store numbers
# list2 = [] # create a list of even numbers
list3 = [] # create a list of positive numbers

while True:
    num = input("Enter a number: ") # user enters input of strings
    if num  == "0": # exit the loop
        break
    else:
        list1.append(int(num)) # adding the element to the empty list

# find positive numbers entered
for num in list1: # iterating each number in list
    if num > 0: # checking condition
        list3.append(int(num))

# find even numbers entered
# for num in list1: # iterating each number in list
#     if num % 2 == 0: # checking condition
#         list2.append(int(num))

# total = sum(list1)
# avg = total/len(list1)
# median = statistics.median(list1)

# print ("Even numbers entered: ", len(list2))
print ("Positive numbers entered: ", len(list3))
# print("Numbers entered in ascending order: ", sorted(list1)) # prints the list of sorted numbers
# print ("Number of items in list: ", len(list1))
# print(f'Total of numbers: {total}, Average of numbers: {avg}')
# print(f'Median: {median}')